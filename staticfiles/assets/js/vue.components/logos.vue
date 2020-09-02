<template>
    <div class="col-12 col-sm-6 col-md-4 py-5">
        <p class="h2 t-brand-light"><img class="lazy" src="/assets/img/loading.gif" :data-src="'/assets/img/logo/'+pic" height=100></p>
        <div class=" f-concert-one t-gray text-lighter">
            {{name}}
        </div>
    </div>
</template>

<script>
    module.exports = {
        data: function () {
            return {}
        },
        props: [
            'name', 'pic', 'comment'
        ]
    }
</script>