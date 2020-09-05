import NormalizeWheel from './../../js/lib/normwheel.js';
import { TweenMax, Linear } from 'gsap';
import './../../js/intlTelInput.js';


const _ = (function() {
  const _screwed = props => {
    const event = typeof props.event === 'undefined' ? 
      'click' : props.event;

    $(document).on(event, props.selector, props.callback);
  };

  function _setPosition($this, $tooltip) {
    var windowWidth = window.innerWidth,
      windowHeight = window.innerHeight,
      tooltipWidth = $tooltip.width(),
      tooltipHeight = $tooltip.height(),
      itemWidth = $this.width(),
      itemHeight = $this.height(),
      offset = $this.offset(),
      leftPosition = offset.left,
      horizontalTooltipVector = leftPosition + itemWidth + 100,
      props = {};

    
    if (horizontalTooltipVector + tooltipWidth > windowWidth) {
      leftPosition = -tooltipWidth;
    } else if (horizontalTooltipVector + tooltipWidth < 0) {
      leftPosition = 0;
    } else {
      leftPosition = '95%';
    }
    props.zIndex = '2';
    props.left = leftPosition;

    $tooltip
      .css(props);
  }

  const _showElement = ($node, state) => {
    TweenMax.to($node, 0.2, {
      opacity: 1,
      onStart: function() {
        $node
          .css('zIndex', 1000)
          .removeClass('visible-hidden');
      },
      onComplete: () => {
        state.opened = true;
      }
    });
  };
  const _hideElement = ($node, state) => {
    TweenMax.to($node, 0.2, {
      opacity: 0,
      onComplete: function() {
        $node
          .addClass('visible-hidden')
          .css('zIndex', -1);
        state.opened = false;
      }
    });
  };

  let _popupStates = {};
  
  const _hideOther = () => {
    const lastOpenedPopup = _popupStates.lastOpenedPopup;

    for ( const popupId in _popupStates ) {
      const popup = _popupStates[popupId];

      if (popupId !== lastOpenedPopup &&
          popup.opened) {
        _hideElement($(popupId), popup);
      }
    }
  };
  const _animatePopup = () => {
    
    $(document).on(
      'click', 
      '.showPopup:not(.closeButton)', 
      function() {
        const $this = $(this);
        
        const popupId = $this.data('popupId');
        let elementState = _popupStates[popupId] || {};
        
        if (!(popupId in _popupStates)) {
          _popupStates[popupId] = elementState;
          elementState = _popupStates[popupId];
          elementState.opened = false;
        } 
        
        const $displayedElement = $(popupId);
        
        if (!elementState.opened) {
          _setPosition($this, $displayedElement);
          _showElement($displayedElement, elementState);
          _popupStates.lastOpenedPopup = popupId;
          _hideOther();
          // elementState.opened = true;
        } else {
          _hideElement($displayedElement, elementState);
          // elementState.opened = false;
        }
        
      });
    
    $(document).on(
      'click', 
      '.closeButton', 
      function() {
        const $this = $(this);
        const popupId = $this.data('popupId');
        const elementState = _popupStates[popupId];
        const $displayedElement = $(popupId);

        if (elementState.opened) {
          _hideElement($displayedElement, elementState);
        }
      });


  };
  return {
    screwed: _screwed,
    show: _showElement,
    hide: _hideElement,
    animatePopup: _animatePopup
  };
}());

const SLIDER = (function() {
  const _state = {
    currentSlide: 1,
    $slider: '',
    isReverse: false
  };
  

  const _init = (sliderSelector, options, isAnimatedSlides=false) => {
    $(function() {
      _state.$slider = $(sliderSelector);
      const $slider = _state.$slider;
      if (!$slider.length) {
        return false;
      }

      $slider.owlCarousel(options);

      $(document).on('keydown', function(e) {
        e.preventDefault();
          
        switch (event.key) {
          case 'ArrowLeft':
            $slider.trigger('prev.owl');
            break;
          case 'ArrowRight':
            $slider.trigger('next.owl');
            break;
          default:
            return; // Quit when this doesn't handle the key event.
        };
      });
      
      $slider.on('wheel', '.owl-stage', function(e) {
        const norm = NormalizeWheel(e.originalEvent);
    
        if (norm.spinY > 0) {
          $slider.trigger('next.owl');
          _state.isReverse = false;
        } else {
          $slider.trigger('prev.owl');
          _state.isReverse = true;
        }
    
        e.preventDefault();
      }); // end load


    });
  };


  return {
    start: _init
  };
}());

SLIDER.start('#mainSlider', {
  loop: true,
  loop: true,
  autoplay: true,
  autoplayTimeout: 6000,
  autoplayHoverPause: true,
  lazyLoad: true,
  items: 1,
  smartSpeed: 1000,
  autoplaySpeed: 1000,
  dots: true
});
SLIDER.start('#catalogs', {
  loop: true,
  autoplay: true,
  autoplayTimeout: 6000,
  autoplayHoverPause: true,
  lazyLoad: true,
  items: 1,
  smartSpeed: 1000,
  autoplaySpeed: 1000,
  dots: false,
  nav: true,
  navText: ['&#8592;', '&#8594;'],
  responsive: {
    480: {
      items: 2,
    }
  }
}, true);

$(function() {
  $('.preloader, .curtains').css({
    'opacity': 0,
    'zIndex': -10000
  });
  $(document).on;

  _.animatePopup();



  $(document).on('click', '.choice__button', function(e) {
    const data = $(this).data();
    const popupId = data.popupId;
    const url = data.src;

    const $figure = $('#figureWithChoice');

    $figure
      .animate({
        opacity: 0
      }, 300, () => {
        $figure
          .css('backgroundImage', `url('${url}')`)
          .data('popupId', popupId)
          .click()
          .animate({
            opacity: 1
          }, 300);
        

      });

      
  }); // end click
  $(document).on('click', '.slideTo', function() {
    $('html, body').animate({
      scrollTop: $($(this).attr('href')).offset().top
    }, 600, Linear.ease);
  });
  $(document).on('click', '.not-follow', function(e) {
	  const url = $(this).attr('href');
	  
	  window.open(url);
	  
	  e.preventDefault();

  }); // end click
});

// if (!Modernizr.placeholder) {
//    $.html5support();
//    $.placeholder(); 
// }


const PHONES = (function() {
  $(function() {
    
    $('#id_callback_phone').intlTelInput({
      initialCountry: 'ru'
    });
  
    $(document).on('input changepropery', '#id_phone_number, #id_callback_phone', function() {
      const $this = $(this);
      let currentValue = $this.val();
      currentValue = currentValue.slice(currentValue.indexOf(' ') + 1);

      if (currentValue.indexOf('+') !== -1)
        return false;
      
      const title = $this.parent().find('.selected-flag').attr('title');
      const code = title.slice(title.lastIndexOf(' ') + 1) + ' ';
      const newValue = code + currentValue;

      $this.val(newValue);
    });
  }); 
}());

const LADDER = (function() {
  const _state = {
    colors: {
      purple: '#654178',
      red: '#99303B'
    },
    prev: 0,
    next: 0,
    current: 0,
    lastColor: ''
  };

  
  const _redColor = _state.colors.red;
  const _purpleColor = _state.colors.purple;

  const _setColors = (invertColor=false) => {
    const $nearestsSteps = $(`.ladderStep[data-index=${_state.next}], .ladderStep[data-index=${_state.prev}]`);
    const index = _state.current;

    _state.current % 3 === 0;
    if (!invertColor) {
      let color = '';
      if (index % 3 === 0) {
        color = _purpleColor;
      } else {
        color = _redColor;
      }

      $nearestsSteps.css('background-color', color);
    } else {
  
      $nearestsSteps.css('background-color', '');
    }

  };
  $(function() {

    $(document).on('mouseenter' , '.ladderStep', function() {
      const $this = $(this);
      const index = $this.data('index');

      _state.current = index;
      _state.prev = index - 1;
      _state.next = index + 1;

      _setColors();
      
    });// end mouseover


    $(document).on('mouseleave' , '.ladderStep', function() {       
      _setColors(true);
    });// end mouseout
  });
}());
