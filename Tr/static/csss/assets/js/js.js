//THIS SECTION IS FOR ANIMATIONS
jQuery(document).ready(function () {
    $('.goals > p').addClass('hideElement');
    $('.type-wrap').removeClass('hideElement');
    $('.map').removeClass('hideElement');

});

$('.up-to-down').viewportChecker({
    classToAdd: 'visible animated fadeIn',
    offset: 200
});
$('.animate-left').viewportChecker({
    classToAdd: 'visible animated fadeInLeftBig',
    offset: 200
});
$('.fadeInUpBi').viewportChecker({
    classToAdd: 'visible animated fadeInUp',
    offset: 200
});
$('.goals > p').viewportChecker({
    classToAdd: 'visible animated fadeInUp',
    offset: 200
});

//THIS SECTION IS FOR SCROLLING EFFECTS
$(function() {
    "use strict";
    $('a[href*=#]:not([href=#])').on( "click", function() {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.substr(1) +']');
        if (target.length) {
            $('html,body').animate({
                scrollTop: target.offset().top - 84
            }, 500);
            return false;
        }
    });
});


//THIS SECTION IS FOR TYPING EFFECTS
$(function(){
    "use strict";
    $("#typed").typed({
//             strings: ["Typed.js a <strong>jQuery</strong> plugin.", "It <em>types</em> out sentences.", "And then deletes them.", "Try it out!"],
        stringsElement: $('#typed-strings'),
        typeSpeed: 60,
        backDelay: 1000,
        loop: true,
        contentType: 'html', // or text
        // defaults to false for infinite loop
        loopCount: false,
        callback: function(){ foo(); },
        resetCallback: function() { newTyped(); }
    });
    $(".reset").on( "click", function() {
        $("#typed").typed('reset');
    });
});
function newTyped(){ /* A new typed object */ }
function foo(){ console.log("Callback"); }

//THIS SECTION IS FOR FIXED HEADER EFFECTS
$(document).scroll(function() {
    "use strict";
    $(".test").text($(this).scrollTop());
    if($(this).scrollTop()>=797){
        $('.navbar').addClass('fixed');
    }
    else{
        $('.navbar').removeClass('fixed');
    }
});

//THIS SECTION IS FOR COUNTER
jQuery(document).ready(function($) {
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });
});
