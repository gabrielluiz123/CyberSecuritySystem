    var sections = $('section.list-me');
    var nav = $('.list-sections');
    sections.each(function(){
        var name = $(this).find('.menu-title').text();
        var data = $(this).children('.container').attr('id');
        var elm = '<li class="menu-item p-3 scroll" data-scroll-to="'+data+'">'+name+'</li>';
        $(elm).appendTo(nav);
    });
