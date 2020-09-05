// jshint esversion: 6
let $toggleButton = $("#toggleButton");

$toggleButton.click((e) => {
    $(e.target).focus();
}); // end click

$('.navItem').not('#navOpportunities, #navRegistr').on('click', (e) => {
  let screenWidth = window.innerWidth;
  if (screenWidth < 768) 
    $('#collapsable').collapse('hide');
}); // end blur

$toggleButton.on('click', (e) => {
  const screenWidth = window.innerWidth;
  if (screenWidth < 768) 
    $('#navOpportunities').addClass('open');
});


$(document).on('click', '#btnTop' ,function()  {
  let $this = $(this);
  $('html, body').stop().animate({
    scrollTop: $($this.attr('href')).offset().top
  }, 500);
  
  return false;
});// end click
const $btnTop = $('#btnTop');


// Кнопка, ведущая наверх
$btnTop.hide();
$(window).scroll((e) => {
  if ($(this).scrollTop() < 100) {
    $btnTop.fadeOut(1000);
  } else {
    $btnTop.fadeIn(1000);
  }  
});// end scroll

// Чтобы не меню не сворачивалось,
// когда нажимаешь на выпадающее меню
$("#navOpportunities").on('click', e => {
  $toggleButton.focus();
});

// Навигация по страницам
// let main = '#mainContent';

//$(document).on('click', '#navHome, #logo', e => {
//  $cmt.showLoading(main);
//  $cmt.switchMenu('#navHome');
//  $cmt.showHomePage();
//});// end click


// $(document).on('click', '#navVideos', e => {
//   $cmt.switchMenu('#navVideos');
//   $cmt.showLoading(main);
//   $cmt.showVideosPage();
// });// end click

// $(document).on('click', '#navContacts', e => {
//   $cmt.switchMenu('#navContacts');
//   $cmt.showLoading(main);
//   $cmt.showContactsPage();
// });// end click

// $(document).on('click', '#navBusiness', e => {
//   $cmt.switchMenu('#navBusiness');
//   $cmt.showLoading(main);
//   $cmt.showBusinessPage();
// });// end click
