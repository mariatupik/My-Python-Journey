$(document).scroll(function () {
    if ($(document).width() < 1024)
        return;

    if ($(document).scrollTop() > $('.full-page').height() / 2)
        $('header').addClass('fixed-header');
    else
        $('header').removeClass('fixed-header');
});

$('.up-btn').on('click', function () {
    $('html, body').animate({
        scrollTop: 0
    }, 1000);
});

$("#show-menu").on('click', function () {
    $('#hidden-menu').animate({
        "right": 0
    }, 500);
});

$("#hidden-menu .close").on('click', function () {
    $('#hidden-menu').animate({
        "right": "-300px"
    }, 500);
});

const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});
