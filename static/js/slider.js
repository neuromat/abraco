$(document).ready(function() {
	// inicia o novo plugin de slider.
    $('#slick-slider').slick({
	  infinite: true,
	  slidesToShow: 3,
	  slidesToScroll: 1,
	  dots: false,
	  speed: 1500,
	  autoplay: true,
	  autoplaySpeed: 6000,
	  adaptiveHeight: true,
	  appendArrows: '#slider-novo',
	  prevArrow: '<a class="left carousel-control" href="#Carousel" data-slide="prev"><i class="glyphicon glyphicon-chevron-left"></i></a>',
	  nextArrow: '<a class="right carousel-control" href="#Carousel" data-slide="next"><i class="glyphicon glyphicon-chevron-right"></i></a>',
      responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3
        }
      },
      {
      breakpoint: 769,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
      },
      {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
     }]
    });
});

