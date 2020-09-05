// jshint esversion: 6

let $callblockForm = $('.callbackForm'),
    $callbackOpenFormBtn = $('#callbackOpenFormBtn'),
    $callbackPhone = $('#id_callback_phone'),
    $callback = $('.callback');

$callblockForm.hide();

$callbackPhone.mask('+7 (000) 000 00 00');

$(document).on('click', '#callbackOpenFormBtn', (e) => {
  $callback.css('z-index', '10000');
  $callblockForm.show('fast');
  $callbackOpenFormBtn.hide(); 
});// end click

$(document).on('click', '#callbackCloseFormBtn', (e) => {
  $callblockForm.hide('fast');
  $callback.css('z-index', '0');
  $callbackOpenFormBtn.show('fast');
});// end click

$(document).on('submit', '#callbackForm', (e) => {
  e.preventDefault();
  registerCallback();
});// end submit

function registerCallback() {
  
  let requestData = {
    'callback_name': $('#id_callback_name').val(),
    'callback_phone': $callbackPhone.val(),
    'callback_message': $('#id_callback_message').val()
  },
  csrftoken = $callblockForm.find('input[name="csrfmiddlewaretoken"]').attr('value');
  
  function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  
  $.ajaxSetup({
      url: '/register_callback/',
      type: 'POST',
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
  
  $.ajax({
    data: requestData,
    success: function(respond) {
      $('#callbackForm').hide();
      
      $callblockForm.append(respond);
    },
    error : function(xhr,errmsg,err) {
      console.log('failure');
    }
  });
}