
require('./lib/vanilla-libs');

$(document).ready(function () {
    require('./lib/on-ready-libs');

    window.onload = function(){
        $('.lazy img').each(function(){
            $(this).attr('src', 'assets/img/loading.gif');
        })
    }   
    /**
     * Define ações padrões da barra de navegação e do botão que leva ao topo da página.
     */
    $(window).on('scroll', function () {
        if ($(this).scrollTop() > 20) {
            setTimeout(function(){
                $('.menu').addClass('bg-navbar-fixed');
            },300);
            $('.menu').removeClass('bg-navbar');
            $('.menu').removeClass('mt-4');
            $('.btn-toTop').addClass('l-faded');
        } else {
            $('.menu').addClass('mt-4');
            $('.menu').addClass('bg-navbar');
            $('.menu').removeClass('bg-navbar-fixed');
            $('.btn-toTop').removeClass('l-faded');
        }
    });

    /**
     * Define açoes padrões para mobile.
     */
    if ($(window).innerWidth() < 574) {
        $('.menu').on('click', function () {
            var height = $(this).children('.menu-item').innerHeight() * ($(this).children('.menu-item').length + 1);
            $(this).toggleClass('opened');
            if ($(this).hasClass('opened')) {
                $(this).css('min-height', height + 'px');
            } else {
                $(this).css('min-height', 0 + 'px');
            }
        });
    }


    /**
     * @var alert
     * Esta variável mapeia todos os elementos do tipo 'alert', para mostrar um simpleAlert
     */
    var alert = $('.alert.not-av');
    /**
     * Esta seção define um alerta único para todos os 'alerts' mapeados. Você pode mudá-la ou excluí-la, de acordo
     * com suas necessidades. Também é possível instanciá-lo dentro do elemento html.
     */
    alert.each(function(){
        $(this).on('click', function(evt){
            evt.preventDefault();
            return simpleAlert.show({
                        message: 'Conteúdo ainda não disponível :/',
                        type: 'danger',
                        gloss: { //Argumento opcional para definir as animações
                            in: 'ease-in', // de entrada 
                            out:'ease-out' // ou saída
                        }
                    });
        })
    });
});


