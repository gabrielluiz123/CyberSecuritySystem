   
    var prlx = $('.parallax');

    $(window).on('scroll', function(){
        /**
         * @var yPos
         * Assiste a medida na qual o usuário já rolou a página
         */
        var yPos = $(this).scrollTop();
        /**
         * @var move
         *  Quantidade que o background será rolado.
         * + move a página na mesma direção do scroll
         * - faz o scroll reverso
         */
        var move = -(yPos / $('.parallax').data('speed'));
        /**
         * @var moveL
         * Quantidade de movimento do parallax para a esquerda
         */
        var moveL= (yPos / $('.parallax-left').data('speed'));
        /**
         * @var moveR
         * Quantidade de movimento do parallax à direito
         */
        var moveR= -(yPos / $('.parallax-right').data('speed'));
        /**
         * Configura o parallax
         */
        $('.parallax').css('top', move + 'px');
        /**
         * Ajuste o lado de scroll configurando o data-scroll-to com o sinal desejado
         *  - move para cima
         *  + move para baixo
         */
        $('.parallax-right').css('left', moveR + 'px');
        $('.parallax-left').css('left', moveL + 'px');
        /**
         * Configura a opacidade do elemento de acordo com sua próproa altura.
         */
        var opacity = 1 - yPos / $('.hideOnScroll').innerHeight()/3;
        /**
         * Ative a propriedade hideOnScroll
         */
        $('.hideOnScroll').css('opacity', opacity);
        
        if($('.hideOnScroll').css('opacity') > 0){
            $('.hideOnScroll').css('transform', 'scale(1)')
        }else{
            $('.hideOnScroll').css('transform', 'scale(0)')           
        }

        
        var st = $(this).scrollTop();
        var wh = $('body').innerHeight();
        var op = 1 - ((st) / wh) * 20;
        var bgp = '50% ' + st / 5 + 'px';

        $('.bg-parallax').css('background-position', bgp);
    });
