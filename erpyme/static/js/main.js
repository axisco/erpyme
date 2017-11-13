$(document).ready(function () {
  $('.collapse').click(function(){
    if ($(this).attr('class') != 'active'){
      $('.collapse-nav').slideUp();
      $(this).next().slideToggle();
      $('.collapse').removeClass('active');
      $(this).addClass('active');
    }
  });
});