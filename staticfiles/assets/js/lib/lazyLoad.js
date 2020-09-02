/* The Lazy Loader works better on the parent element like sections */
var thumb_folder = 'thumb/';
$('.lazy').each(function () {
    var section = this;
    $(window).on('scroll', function () {

        var yPos = $(this).scrollTop();

        var ofst = $(section).offset().top - 500;
        if (yPos >= ofst) {
            loadImage(section);
        }
    });
    if($(section).hasClass('modal')){
        $(document).on('show.bs.modal', function(){
            loadImage(section);
        })
    }
});
 
function loadImage(section){
    var el = $(section).find('img.lazy');
    el.each(function () {
        var img = new Image();
        var src = $(this).data('src');
        var el = this;
        img.src = src;
        el.src = src;
    })
}