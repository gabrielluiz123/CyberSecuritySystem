<template>
    <div class="col-12 col-md-6">
        <div class="col-12 py-5  t-section text-center ">
            <img class="lazy w-25" :data-src="'/assets/img/logo/'+pic">
        </div>
        <div class="col-12 col-12 py-5 ">
            <!-- <h4 class="text-left">Wordpress</h4> -->
            <div class="text-justify f-concert-one t-highlight-dark">
                {{comment}}
            </div>
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