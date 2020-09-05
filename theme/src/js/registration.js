import './lib/jquery.mask.js';
import './intlTelInput.js';

const REGISTRATION = (function() {
  const that = {};
  const _assert = (condition, message, SomeError=Error) => {
    if (condition) {
      throw new [SomeError](message);
    }
  };


  const masks = {
    passport: {
      current: '0000-000000',
      idChoices: 'passportChoises',
      inputId: 'id_passport_data',
      pattern: {'translation': {
    	A: {pattern: /[A-Za-zа-яА-Я]/}
    	
    	
  	  	}
  	  },
      masks: [
        {
          mask: '0000-000000',
          value: 'Россия'

        },
        {
          mask: 'AA000000',
          value: 'Україна'

        },
        {
          mask: 'AA0000000',
          value: 'Белоруссия'

        },
        {
          mask: 'AA000000',
          value: 'Литва'

        },
        {
          mask: 'AA0000000',
          value: 'Латвия'

        },
        {
          mask: 'A0000000',
          value: 'Эстония'

        },
        {
          mask: 'AA0000000',
          value: 'Армения'

        },
        {
          mask: 'A0000000',
          value: 'Казахстан'

        },
        {
          mask: 'AA0000000',
          value: 'Киргизия'

        },
        {
          mask: 'AA 00 00000',
          value: 'Узбекистан'

        },
        {
          mask: 'A0000000',
          value: 'Туркменистан'
        },
        {
          mask: '000000',
          value: 'Израиль'
        },
        {
          mask: 'A000000',
          value: 'Индонезия'
        },
        {
          mask: '000000000',
          value: 'США'
        },
        {
          mask: false,
          value: 'Другое'
        }
      ]
    }
  };

  const $phone = $('#id_phone_number');
  const $passport = $(`#${masks.passport.inputId}`);

  const _maskHandler = {
    set: ($node, mask, pattern) => {
      $node.mask(mask, pattern);
    },
    get: (id) => {
      const mask = $(id).data('mask');
      _assert(
        typeof mask === 'undefined', 
        'Choice has no mask!'
      );
      
      return mask;  
    }, 
    clear: $node => {
      $node.unmask();
    }
  };

  const doWithMaskObject = (masks, callback) => {
    for (const mask in masks) {
      callback(masks[mask]);    
    }
  };

  const _getChoicesIds = masks => {
    let choicesIds = [];

    doWithMaskObject(masks, maskObject => {
      choicesIds.push(`#${maskObject.idChoices}`);
    });
    return choicesIds.join(',');
  };

  const _initMasks = masks => {
    doWithMaskObject(masks, maskObject => {
    	const $field = $(`#${maskObject.inputId}`);
    	$field.attr('placeholder', maskObject.current);
      	_maskHandler.set(
        	$field,
        	maskObject.current,
        	maskObject.pattern
      	);
    });
  };

  
    
  const _switchMask = (masks, id, choosenMask) => {
    doWithMaskObject(masks, maskObject => {
      if (maskObject.idChoices === id) {
        if (choosenMask === 'false') {
          // $(`#${maskObject.inputId}`).unmask();
          _maskHandler.clear($(`#${maskObject.inputId}`));
        } else {
          maskObject.current = choosenMask;
          _initMasks(masks);
        }

      }
    });

  };


  /*
   * Компонует опции  для select.
   *
   * @param {Object} $select - Узел, куда будут впрыскивать опции. 
   * @param {Array} options - опции селекта.
   * 
   */ 
  const _createSelectOptions =  ($select, options) => {
    let resultHtml = '';
      
    options.forEach(option => {
      resultHtml += `
          <option 
            value="${option.mask}" 
            class="userMask"
          >
            ${option.value}
          </options>`;

        
        
        
    });
      
    $select.html(resultHtml);


    return $select;
  };

  /*
   * Компонует выбор масок в теге select.
   *
   * @param {String} id - Идентификатор поля выбора. 
   * @param {Array} options - Массив объектов описывающие опции выбора маски. 
   * 
   */ 
  const _createSelect = (id, options) => {
    const $select = $(`<select id='${id}'>`);
    $select.addClass('controller__input controller__input_select controller__input_red');
      
    return _createSelectOptions($select, options);
  };

  /*
   * Компонует выборы масок и добавляет их к нужным полям.
   *
   * @param {Array} selects - Массив объектов описывающие выборки. 
   * 
   */ 
  const _addChoices = selects => {
    for (const key in selects) {
      const select = selects[key];
      const $select = _createSelect(select.idChoices, select.masks);

        
      const $parent = $(`#${select.inputId}`).parent();
        
      $parent.append($select);
    }
  };

  const _initFormFields = masks => {

    _initMasks(masks);

    $('#subButton').prop('disabled', true);
   
    _addChoices(masks);

    $phone.intlTelInput({
      initialCountry: 'ru'
    });
  };

  // Обновляет каждое слово с большой буквы.
  const _titleCase = ($selector, str) => {
    str = str
      .toLowerCase()
      .split(' ')
      .map( function(word) {
        return word.replace(word.charAt(0), word.charAt(0).toUpperCase());
      })
      .join(' ');
      
    $selector.val(str);
  };
  // Обновляет поле без пробелов, с большой буквы одно слово.
  let fixText = val => {
    let arr = val.split(' ');
      
    arr[0] = arr[0][0].toUpperCase() +
               arr[0].slice(1);
      
    return arr[0];
  };

  const _updateField = ($field, val) => {
    if (val.length !== 0)
      $field.val(fixText(val));
  };

  $(function() {
    _initFormFields(masks);

    $(document).on('change', _getChoicesIds(masks), function() {
      const $this = $(this);
      const mask = $this.val();
      const id = $this.attr('id');

      _switchMask(masks, id, mask);
          
    });
    // Форматирование первой буквы слова, с возможностью добавлять ещё одно слово через дефис, но не через пробел.
    $(document).on('input changepropery', '#id_last_name, #id_first_name, #id_middle_name', (e) => {
      let $firstName = $('#id_first_name'),
        $lastName = $('#id_last_name'),
        $middleName = $('#id_middle_name'),
        fNameVal = $firstName.val(),
        lNameVal = $lastName.val(),
        mNameVal= $middleName.val();
        
      _updateField($firstName, fNameVal);
      _updateField($lastName, lNameVal);
      _updateField($middleName, mNameVal);
    }); // end input changeproperty

    // Простое форматирование в верхний регистр первых букв
    $(document).on('input changepropery', ' #id_street, #id_region, #id_city', (e) => {
      let $street = $('#id_street'),
        $city = $('#id_city'),
        $region = $('#id_region'),
        streetVal = $street.val(),
        cityVal = $city.val(),
        regionVal = $region.val();
          
      _titleCase($region, regionVal);
      _titleCase($city, cityVal);
      _titleCase($street, streetVal);
    });
  
    $(document).on('click', '#checkReady', () => {
      let $checkReady = $('#checkReady');
      let $subButton = $('#registrataionSubmitButton');

      if ($checkReady.prop('checked'))
        $subButton.prop('disabled', false);
      else 
        $subButton.prop('disabled', true);  
    }); // end click
    // $(document).on('click', '#id_empty_middle_name', (e) => {
    //   let $checkboxEmptyField = $('#id_empty_middle_name'),
    //       $middleName = $('#id_middle_name'),
    //       $controller = $middleName.parent();
        
    //   if ($checkboxEmptyField.prop('checked')) {
    //     $controller.hide('fast');
    //   } else {
    //     $controller.show('fast');   
    //   }
    // }); // end click   

  }); // end load
  // Автозаполнение поля города и области
}());
