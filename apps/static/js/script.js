(function ($) {

  "use strict";

  var initSlider = function () {
    var swiper = new Swiper(".main-swiper", {
      slidesPerView: 3,
      spaceBetween: 80,
      speed: 700,
      loop: true,
      navigation: {
        nextEl: '.icon-arrow-right',
        prevEl: '.icon-arrow-left',
      },
      breakpoints: {
        300: {
          slidesPerView: 1,
          spaceBetween: 20,
        },
        768: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        1200: {
          slidesPerView: 3,
          spaceBetween: 80,
        },
      },
    });

    // swiper slider home 2
    var swiper = new Swiper(".slideshow", {
      slidesPerView: 1,
      spaceBetween: 0,
      speed: 1000,
      loop: true,
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      navigation: {
        nextEl: '.icon-arrow-right',
        prevEl: '.icon-arrow-left',
      }
    });

    // two colum swiper slide
    var swiper = new Swiper(".two-column-swiper .swiper", {
      slidesPerView: 1,
      loop: true,
      speed: 900,
      // direction: "vertical",
      navigation: {
        nextEl: ".two-column-swiper .icon-arrow-right",
        prevEl: ".two-column-swiper .icon-arrow-left",
      },
    });

    var swiper = new Swiper(".overlay-swiper", {
      slidesPerView: "auto",
      loop: true,

      navigation: {
        nextEl: ".icon-arrow-right",
        prevEl: ".icon-arrow-left",
      },
    });

    $('.product-carousel').each(function () {
      var sectionId = $(this).attr('id');
      var swiper = new Swiper("#" + sectionId + " .swiper", {
        slidesPerView: 4,
        spaceBetween: 20,
        navigation: {
          nextEl: "#" + sectionId + " .icon-arrow-right",
          prevEl: "#" + sectionId + " .icon-arrow-left",
        },
        breakpoints: {
          0: {
            slidesPerView: 1,
            spaceBetween: 20,
          },
          768: {
            slidesPerView: 3,
            spaceBetween: 10,
          },
          1366: {
            slidesPerView: 4,
            spaceBetween: 40,
          },
        },
      });
    })

    var swiper = new Swiper(".testimonial-swiper", {
      effect: "coverflow",
      grabCursor: true,
      centeredSlides: true,
      loop: true,
      slidesPerView: "auto",
      coverflowEffect: {
        fade: true,
      },
      pagination: {
        el: ".testimonial-swiper-pagination",
        clickable: true,
      },
    });

    var swiper = new Swiper(".review-swiper", {
      slidesPerView: 1,
      spaceBetween: 20,
      loop: true,
      navigation: {
        nextEl: ".icon-arrow-right",
        prevEl: ".icon-arrow-left",
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });

    // product single page
    var thumb_slider = new Swiper(".product-thumbnail-slider", {
      slidesPerView: 4,
      spaceBetween: 0,
      autoplay: true,
      direction: "horizontal",
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });

    var large_slider = new Swiper(".product-large-slider", {
      slidesPerView: 1,
      autoplay: true,
      spaceBetween: 0,
      effect: 'fade',
      thumbs: {
        swiper: thumb_slider,
      },
    });

  };

  // input spinner
  var initQuantitySpinner = function () {

    $('.product-qty').each(function () {

      var $el_product = $(this);
      var quantity = 0;

      $el_product.find('.quantity-right-plus').click(function (e) {
        e.preventDefault();
        var quantity = parseInt($el_product.find('#quantity').val());
        $el_product.find('#quantity').val(quantity + 1);
      });

      $el_product.find('.quantity-left-minus').click(function (e) {
        e.preventDefault();
        var quantity = parseInt($el_product.find('#quantity').val());
        if (quantity > 0) {
          $el_product.find('#quantity').val(quantity - 1);
        }
      });

    });

  }

  // init jarallax parallax
  var initJarallax = function () {
    jarallax(document.querySelectorAll(".jarallax"));

    jarallax(document.querySelectorAll(".jarallax-keep-img"), {
      keepImg: true,
    });
  }

  // Animate Texts
  var initTextFx = function () {
    $('.txt-fx').each(function () {
      this.innerHTML = this.textContent.replace(/\S/g, "<span class='letter'>$&</span>");
    });
  }

  var initScrollNav = function () {
    var scroll = $(window).scrollTop();
    if (scroll >= 200) {
      $('.navbar.fixed-top').addClass("bg-white");
      $('.navbar.fixed-top').addClass("text-black");
      $('.navbar.fixed-top').removeClass("text-white");
      $('#offcanvasNavbar2').removeClass("bg-dark");
    } else {
      $('.navbar.fixed-top').removeClass("bg-white");
      $('.navbar.fixed-top').removeClass("text-black");
      $('.navbar.fixed-top').addClass("text-white");
      $('#offcanvasNavbar2').addClass("bg-dark");
    }
  }




  // init Isotope
  var initIsotope = function () {
    $('.grid').each(function () {

      var $buttonGroup = $('.button-group');
      var $checked = $buttonGroup.find('.is-checked');
      var filterValue = $checked.attr('data-filter');

      var $grid = $('.grid').isotope({
        itemSelector: '.product-item',
        layoutMode: 'fitRows',
        filter: filterValue
      });

      // bind filter button click
      $('.button-group').on('click', 'a', function (e) {
        e.preventDefault();
        filterValue = $(this).attr('data-filter');
        $grid.isotope({ filter: filterValue });
      });

      // change is-checked class on buttons
      $('.button-group').each(function (i, buttonGroup) {
        $buttonGroup.on('click', 'a', function () {
          $buttonGroup.find('.is-checked').removeClass('is-checked');
          $(this).addClass('is-checked');
        });
      });

    });
  }

  var searchPopup = function () {
    // open search box
    $('.navbar').on('click', '.search-button', function (e) {
      $('.search-popup').toggleClass('is-visible');
    });

    $('.navbar').on('click', '.btn-close-search', function (e) {
      $('.search-popup').toggleClass('is-visible');
    });

    $(".search-popup-trigger").on("click", function (b) {
      b.preventDefault();
      $(".search-popup").addClass("is-visible"),
        setTimeout(function () {
          $(".search-popup").find("#search-popup").focus()
        }, 350)
    }),
      $(".search-popup").on("click", function (b) {
        ($(b.target).is(".search-popup-close") || $(b.target).is(".search-popup-close svg") || $(b.target).is(".search-popup-close path") || $(b.target).is(".search-popup")) && (b.preventDefault(),
          $(this).removeClass("is-visible"))
      }),
      $(document).keyup(function (b) {
        "27" === b.which && $(".search-popup").removeClass("is-visible")
      })
  }

  $(window).scroll(function () {
    initScrollNav();
  });


  $(window).load(function () {
    $(".preloader").addClass("loaded");

    $(".btn-nav").on("click tap", function () {
      $(".nav-content").toggleClass("showNav hideNav").removeClass("hidden");
      $(this).toggleClass("animated");
    });
  });





  // document ready
  $(document).ready(function () {
    searchPopup();
    initJarallax();
    initTextFx();
    initQuantitySpinner();
    initSlider();
    initIsotope();


    $(".youtube").colorbox({
      iframe: true,
      innerWidth: 960,
      innerHeight: 585
    });

    AOS.init({
      duration: 1200,
      once: true,
    })

    var Sticky = new hcSticky('.sticky-info', {
      stickTo: 'section.single-product',
      innerTop: 200,
      // followScroll: false,
      responsive: {
        980: {
          disable: true
        }
      }
    });



  }); // document ready

})(jQuery)


// 
let votesA = 0;
let votesB = 0;

function vote(option) {
    if (option === 'A') {
        votesA++;
        document.getElementById('votesA').textContent = votesA;
    } else if (option === 'B') {
        votesB++;
        document.getElementById('votesB').textContent = votesB;
    }
}


const prevButton = document.getElementById('prevBtn');
const nextButton = document.getElementById('nextBtn');
const slideshowContainer = document.querySelector('.slideshow-container');
const images = document.querySelectorAll('.slideshow-container img');
let currentIndex = 0;

// 前の画像に移動する関数
function prevSlide() {
    if (currentIndex === 0) {
        currentIndex = images.length - 1;
    } else {
        currentIndex--;
    }
    updateSlide();
}

// 次の画像に移動する関数
function nextSlide() {
    if (currentIndex === images.length - 1) {
        currentIndex = 0;
    } else {
        currentIndex++;
    }
    updateSlide();
}

// スライドを更新する関数
function updateSlide() {
    images.forEach((image, index) => {
        if (index === currentIndex) {
            image.style.display = 'block';
        } else {
            image.style.display = 'none';
        }
    });
}

// 前のボタンと次のボタンにクリックイベントを追加
prevButton.addEventListener('click', prevSlide);
nextButton.addEventListener('click', nextSlide);

// 初期表示
updateSlide();



// This is "probably" IE9 compatible but will need some fallbacks for IE8
// - (event listeners, forEach loop)

// wait for the entire page to finish loading
window.addEventListener('load', function() {
	
	// setTimeout to simulate the delay from a real page load
	setTimeout(lazyLoad, 1000);
	
});

function lazyLoad() {
	var card_images = document.querySelectorAll('.card-image');
	
	// loop over each card image
	card_images.forEach(function(card_image) {
		var image_url = card_image.getAttribute('data-image-full');
		var content_image = card_image.querySelector('img');
		
		// change the src of the content image to load the new high res photo
		content_image.src = image_url;
		
		// listen for load event when the new photo is finished loading
		content_image.addEventListener('load', function() {
			// swap out the visible background image with the new fully downloaded photo
			card_image.style.backgroundImage = 'url(' + image_url + ')';
			// add a class to remove the blur filter to smoothly transition the image change
			card_image.className = card_image.className + ' is-loaded';
		});
		
	});
	
}

