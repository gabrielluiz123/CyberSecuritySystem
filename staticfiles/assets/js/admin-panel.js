var data = {
    pages: [],
    onRequest: false,
    pageTitle: "",
    pageSubtitle: "",
    pageRoute: "",
    pageSearch: "",
}

var page = new Vue({
    el: '#pages_pane',
    data: data,
    methods: {
        getPages: function()
        {
            if(data.onRequest) return false;

            data.onRequest = true;
            $.post('/api/pages', {
                exec: 'request_pages'
            }, null, 'json').then(function(r){
                if('erro' in r){
                    simpleAlert.show({
                        message: 'Houve um problema ao carregar suas páginas..'
                    });
                }else{
                    data.pages = r;
                }
                data.onRequest = false;
            });
        },
        createPage: function()
        {
            if(data.onRequest || data.pageRoute.length < 3) return simpleAlert.show({
                message: 'Sua rota necessita de ao menos três caracteres!'
            });
            
            data.onRequest = true;
            $.post('/api/pages', {
                exec: 'create_page',
                page: {
                    title: data.pageTitle,
                    subtitle: data.pageSubtitle,
                    route: data.pageRoute,
                }
            }, null, 'json').then(function(r){
                if('erro' in r){
                    simpleAlert.show({
                        message: 'Algo deu errado.. tente novamente.'
                    });
                }else{
                    simpleAlert.show({
                        message: 'Página criada com sucesso!',
                        type: 'success'
                    });
                }
                data.onRequest = false
                page.getPages();

            });
        },
        removePage: function()
        {

        },
        resetForm: function()
        {
            data.pageRoute = data.pageTitle = data.pageSubtitle = "";
        },
        replaceWhiteSpaces: function(e)
        {
            var nstr =  (e.target.value.replace(/\s/g, "-"));
            e.target.value = nstr.toLocaleLowerCase();
        }
    },
    created: function()
    {
        this.getPages();
    }
})

let albumData = {
    albums: [],
    photos: [],
    albumId: "",
    cookedDeletion: "",
    editingPhotoIdx: "none",
    editingPhotoText: "",
    editingAlbumTitle: "none",
    editingAlbumDescription: 'none',
    curAlbum: 'none',
    fileInputs: [
        0,
    ],
    cookedAlbum: ''
}

let alb = new Vue({
    el:"#album_pane",
    data:albumData,
    methods: {
        getAlbums: function()
        {
            $.post('api/album/update', {
                exec: 'get_albums'
            },null, 'json').then(function(r){
                if(!r.err){
                    albumData.albums = null;
                    albumData.albums = r;
                    alb.getPhotos(0)
                }else{
                    return simpleAlert.show({
                        message: 'Houve algum problema ao buscar álbuns..'
                    });
                }
            })
        },
        getPhotos: function(idx)
        {
            if(albumData.fileInputs.length > 1){
                $('#confirm_change').modal('show');
                albumData.cookedAlbum = idx;
            }else{
                $.post('api/albums',{
                    exec: "get_album",
                    albumId: albumData.albums[idx].id
                }, null, 'json').then(function (r) {
                    albumData.photos = null;
                    albumData.photos = r;
                    albumData.albumId = albumData.albums[idx].id;
                    albumData.curAlbum = albumData.albums[idx];
                    albumData.curAlbum.idx = idx;
                });
            }  
        },
        resetForm: function()
        {
            albumData.fileInputs = [0];
            $($('input[type=file]')[1]).parent('label').removeClass('d-none');
            $($('input[type=file]')[1]).val("");
            this.getPhotos(albumData.cookedAlbum);
        },
        deletePhoto: function ()
        {
            if(albumData.cookedDeletion != undefined){
                $.post('api/album/update', {
                    exec: 'delete_photo',
                    id: albumData.photos[albumData.cookedDeletion].id
                }, null, 'json').then(function(r){
                    var t = 'warn';

                    if(!r.err){
                        t = 'success';
                        albumData.photos.splice(albumData.cookedDeletion, 1);
                    }

                    simpleAlert.show({
                        message: r.res,
                        type: t
                    })
                });
                
            }
            
        },

        saveTitle: function()
        {
            $.post('api/album/update', {
                exec:'update_album_title',
                name: albumData.curAlbum.name,
                id: albumData.curAlbum.id
            }, null, 'json').then(function(r){
                var t = 'warn';
                if(!r.err){
                    t = 'success';
                    albumData.albums[albumData.curAlbum.idx].name = albumData.curAlbum.name;
                    albumData.editingAlbumTitle = 'none';
                }
                simpleAlert.show({
                    message: r.res,
                    type: t
                })
            })
        },

        saveDescription: function()
        {
            $.post('api/album/update', {
                exec: 'update_photo_description',
                id: albumData.photos[albumData.editingPhotoIdx].id,
                description: albumData.editingPhotoText
            }, null, 'json').then(function(r){
                var t = 'warn';
                if(!r.err){
                    t = 'success';
                    albumData.photos[albumData.editingPhotoIdx].desc = albumData.editingPhotoText;
                    albumData.editingPhotoText = "";
                    albumData.editingPhotoIdx = 'none';
                }
                simpleAlert.show({
                    message: r.res,
                    type: t
                })
            })
        },

        insertPhotosToAlbum(el)
        {
            var form = $(el.target).parent('form')[0];

            let formData = new FormData(form);
            $.ajax({
                url: 'api/album/update',
                data: formData,
                type: 'POST',
                contentType: false, // NEEDED, DON'T OMIT THIS (requires jQuery 1.6+)
                processData: false, // NEEDED, DON'T OMIT THIS
                success: function(r){
                    var t = 'warn';
                    if(!r.err){
                        t = 'success';
                        albumData.cookedAlbum = albumData.curAlbum.idx;
                        alb.resetForm();
                    }
                    simpleAlert.show({
                        message: r.res,
                        type: t
                    })

                }
            });
            
        },

        addPhotoToCurrentAlbum: function (evt)
        {
            var el = evt.target;
            var p = {
                url:	URL.createObjectURL(el.files[0]),
                desc:	'Envie as fotos para alterar a descrição.',
                album:	'null',
                id: null
            };

            albumData.fileInputs.push(albumData.fileInputs.length)
            albumData.photos.push(p);
            $(el).parent('label').addClass('d-none');
        },

        updateAlbumDescription: function()
        {
            $.post('api/album/update', {
                exec: 'update_album_description',
                id: albumData.curAlbum.id,
                description: albumData.curAlbum.desc
            }, null, 'json').then(function(r){
                var t = 'warn';
                if(!r.err){
                    t = 'success';
                    albumData.albums[albumData.curAlbum.idx].desc = albumData.curAlbum.desc;
                    albumData.editingAlbumDescription = 'none';
                }
                simpleAlert.show({
                    message: r.res,
                    type: t
                })
            })
        },
        updateThumbnail: function(e)
        {
            let el = e.target;

            let formData = new FormData();
            formData.append('thumb', el.files[0]);
            formData.append('exec', 'update_album_thumbnail');
            formData.append('albumId', albumData.curAlbum.id);
            $('#album-thumbnail img').attr('src', 'assets/loading.gif');

            $.ajax({
                url: 'api/album/update',
                data: formData,
                type: 'POST',
                contentType: false, 
                processData: false, 
                success: function(r){
                    var t = 'warn';
                    if(!r.err){
                        t = 'success';

                        albumData.albums[albumData.curAlbum.idx].thumb = r.path;
                        $('#album-thumbnail img').attr('src', URL.createObjectURL(el.files[0]));

                    }
                    simpleAlert.show({
                        message: r.res,
                        type: t
                    })

                }
            });
            

        }
    },
    created: function(){
        this.getAlbums();
    }
})

let deleteModal = new Vue({
    el: '#album_modal',
    data: {},

    methods: {
        deletePhoto(){alb.deletePhoto()}
    }
})
let changeModal = new Vue({
    el: '#confirm_change',
    data: {},

    methods: {
        resetForm(){alb.resetForm()}
    }
})
