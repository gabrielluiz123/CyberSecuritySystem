    
    /**
     * Este método realiza o "reveal" da  seção, isto é,
     * carrega a seção apenas quando o usuário está vendo
     * na viewport.
     */

    
    $('.reveal').each(function()
    {
        /**
         * @var section
         * Esta é a seção na qual terá o "reveal" ativo
         */
        var section = this;
        /**
         * @var ctUp
         * Esta variável representa o elemento de countup, responsável por rodar a animação de 0 até o 
         * numero destino
         */
        var ctUp = $(section).find('.countup');

        $(window).on('scroll resize', function()
        {
            /**
             * @var yPos
             * esta é a distância a qual o usuário já rolou a página
             */
            var yPos = $(this).scrollTop();
            /**
             * @var ofst
             * Esta té a distância do topo  da página (ypos === 0) até o topo do elemento seção
             */
            var ofst = $(section).offset().top - 200;
            /**
             * @var s
             * Este é o elemento filho da seção que sofrerá as alterações para ser carregado
             */
            var s =   $(section).children('div')
            .children('.row')

            /**
             * Esta parte da função define a quantidade de rolagem que acontecerá até o conteúdo ser mostrado.
             * Em nosso caso, definimos um padrão de 85% de rolagem da diferença do topo da ṕágina (yPos === 0)
             * até o topo da seção. Então, adiciona-se a classe desejada. Você pode criar mais classes e estilos
             * de aparição no arquivo reveal.scss e definí-los aqui.
             */
            if(yPos >= ofst){
                if($(section).hasClass('l-fade-scroll')){
                  s.addClass('l-scrolled');
                }else{
                    s.addClass('l-faded');
                }
                countUp(ctUp);
                ctUp = null;
            }
        });
    });

let countUp = function(el){
    $(el).each(function(){
        var c = 0;
        var el = this;
        var add = $(el).data('count')/100
        el.countUp = setInterval(function(){
            if(c < $(el).data("count")){
                c+=add;
            }else{
                $(el).removeClass("countup");
                clearInterval(el.countUp);
            }
            $(el).text(c);
        },10);
    })
}