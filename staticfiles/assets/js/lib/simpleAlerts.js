
global.simpleAlert = function() 
{
    return this;
}
simpleAlert.shown;

/**
 * Este método global é responsável por definir as configuraçãoes do simpleAlert e mostrá-lo.
 * @var options opções de configuração do alerta.
 */
simpleAlert.show = function(options)
{
    /**
     * @var id
     * Define uma ID para o elemento
     */
    var id      = new Date().getUTCMilliseconds();
    /**
     * @var type
     * Define o tipo de alerta (classe css). Padrão definido como 'warn'
     */
    var type    = 'warn';
    /**
     * @var message 
     * Define uma mensagem a ser mostrada no alerta
     */
    var message = 'Sua mensagem aqui';
    /**
     * @var icon 
     * Define um ícone a ser mostrado no alerta baseado no fontAwesome 4 veja https://fontawesome.com
     */
    var icon    = 'fa-exclamation-circle';
    /**
     * @var ttl
     * Define um 'Time to Leave' do alerta, isto é, o tempo que ele demorará para desaparecer
     */
    var ttl     = 3000;
    /**
     * @var dismissable
     * Define se o alerta desaparece com um clique ou não. Padrão: true
     */
    var dismissable = true;
    /**
     * @var gloss
     * Define o tipo de animação do alerta ao aparecer/desaparecer
     */

    /**
     * @var fontColor
     * Define a classe de cor do texto
     */
    var fontColor = 't-white';
    var gloss = {
        in: 'cubic-bezier(.54,.3,.39,1.58)',
        out:'cubic-bezier(.59,-0.53,.57,.78)'
    }

    /**
     * Opções configuradas para o alerta. Abaixo estão as condições de configuração. Não modifique, caso não
     * saiba o que está fazendo ;)
     * Você pode adicionar mais tipos de opções, caso queira.
     */
    options.type != null        ? type = options.type           : type;
    options.message != null     ? message = options.message     : message;
    options.icon != null        ? icon = options.icon           : icon;
    options.ttl != null         ? ttl = options.ttl             : ttl;
    options.dismissable != null ? dismissable = options.dismissable : dismissable;
    options.fontColor != null ? fontColor = options.fontColor : fontColor;
    if(options.gloss != null){
        options.gloss.in != null    ? gloss.in = options.gloss.in   : gloss;
        options.gloss.out != null   ? gloss.out = options.gloss.out  : gloss;
    }
    
    type === 'warn'     ? icon = 'fa-exclamation-circle': false;
    type === 'danger'   ? icon = 'fa-skull'             : false;
    type === 'success'  ? icon = 'fa-check-circle'      : false;

    if(simpleAlert.isShowing()){
        simpleAlert.hide(simpleAlert.shown, 0, gloss);
    }
    
    $('body').append('<div class="simple-alert container d-flex justify-content-center alert" id="'+id+'" style="transform: scale(0)"><div class="row '+type+' '+fontColor+'"><div class="simple-symbol col-1"><i class="fas '+icon+'"></i></div><div class="simple-body col-10">'+message+'</div></div></div>');
    var elem = $('#'+id);

    
    setTimeout(function(){

        $('#'+id)
        .css('transition', gloss.in+' 300ms')
        .css('transform', 'scale(1)')
    }, 100);
    
    if(dismissable){
        $('#'+id).on('click', function(){
            simpleAlert.hide(id, 0, gloss);
        })
    }

    simpleAlert.shown = id;
    simpleAlert.hide(id, ttl, gloss);

    return true;
}
/**
 * Este método é responsável por esconder e remover o alerta mostrado em determinada
 * situação, definido em @method simpleAlert.show()
 */
simpleAlert.hide = function(id, ttl, gloss)
{
    if(gloss == null) var gloss = {out: 'cubic-bezier(.59,-0.53,.57,.78)'};
    setTimeout(function(){
        $('#'+id)
        .css('transition', gloss.out+' 300ms')
        .css('transform', 'scale(0)');
        setTimeout(function(){
            $('#'+id).remove();
        }, 300);
    },ttl);
}
simpleAlert.isShowing = function()
{
    return simpleAlert.shown !== null;
}
