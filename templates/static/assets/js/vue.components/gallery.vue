<template>
    <div class="album col-sm-4 lazy showcase-album">
        <h5 class="text-center">{{title}}</h5>
        <img class="lazy pointer" data-target="#photoLightBox" data-toggle="modal" :data-src="thumb" />
        <div class="t-gray" v-html="desc"></div>
    </div>
</template>

<script>
    module.exports = {
        data: function () {
            return {}
        },
        props: [
            'thumb', 'title', 'desc', 'albumId'
        ]
    }
</script>