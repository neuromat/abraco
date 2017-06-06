$('.multi-item-carousel').carousel({
  interval: 15000
});
$('.multi-item-carousel .carousel-inner .item').each(function(){
  if($(window).width() > 1000){
    var next = $(this).next();
    if (!next.length) {
      next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));
    if (next.next().length>0) {
      next.next().children(':first-child').clone().appendTo($(this));
    } else {
      $(this).siblings(':first').children(':first-child').clone().appendTo($(this));
    }
  }
});