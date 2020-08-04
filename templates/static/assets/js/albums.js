import {Carousel, Slide} from 'vue-carousel';
window.onload = function(){};
let photoGallery = {
    photos: []

}

let gallery = {
    albums: [],
    brands: []
}


let aco = new Vue({
    el: "#gallery",
    data: gallery,
    components:{
        Carousel, Slide
    },
    methods: {
        setAlbum: function (id) {
            if (id != null && id != undefined) {
                $.post('api/albums', {
                    exec: "get_album",
                    albumId: id
                },null, 'json').then( r => {
                    this.brands = r;
                    console.log(this.albums);
                })
            }
        },
        getAlbums: function()
        {
            if(onRequest) return false;
            onRequest = true;
            $.post('api/albums', {
                exec: 'get_all_albums'
            }, null, 'json').then( r => {
                this.albums = r;
                console.log('albums loaded');
                this.setAlbum(this.albums[0].id);
                requestRelease();
            });
        }
    },
    created: function () {
        this.getAlbums();
    }
})

let gal = new Vue({
    el: "#photoLightbox",
    data: photoGallery,

    methods: {
        releaseAlbum: function () {
            this.photos = [];
        }
    },
    created: function () {
        $(window).on('hidden.bs.modal', function () {
            setTimeout(function () {
                gal.releaseAlbum();
            }, 100)
        })
    }
})