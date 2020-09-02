

    var scroll = $('.scroll');
    var position;
    scroll.on('click', function (e) {
        e.preventDefault();
        var scrollTo = $(this).data('scrollTo');
        var ofst = position = $('#' + scrollTo).offset().top;
        if ($(this).parents('.menu').length > 0) {
            position -= $(this).innerHeight() - 10;
        }
        $('html, body').animate({
            scrollTop: position
        }, 500, );
    });

    var nav = $('.menu .menu-item');
    var wh   = window.innerHeight;
    var section = $('section');
    $(section).each(function(){

        var tgt  = $(this).children('div').attr('id');
        var parent=$(this).parent().attr('id');
        var ofst = $(this).offset().top -200;

        $(window).on('scroll', function(){
            var yPos = $(this).scrollTop();
            if(yPos >= ofst && yPos <= (ofst+wh)){
                nav.each(function(){
                    var id = '#'+$(this).attr('id');
                    if(($(this).attr('data-scroll-to') == tgt || $(this).attr('data-scroll-to') == parent) 
                    &&  $(this).attr('data-scroll-to') != undefined){
                        $(this).addClass('highlight');
                    }else{
                        $(this).removeClass('highlight');
                    }
                });
            }

        });
    });
