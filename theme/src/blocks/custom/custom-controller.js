// jshint esversion: 6

$('.preloader, .curtains').css({
	'opacity': 0,
	'zIndex': -10000
});

$(document).on('click', '.not-follow', function(e) {
  const url = $(this).attr('href');
  
  window.open(url);
  
  e.preventDefault();
}); // end click

// Тесты
// if (!Modernizr.placeholder) {
//    $.html5support();
//    $.placeholder(); 
// }

//= ../header/callback/callback.js