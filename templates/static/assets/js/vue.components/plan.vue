<template>
    <div class="col-12 col-sm-3 mx-3 shadow py-3 rounded-10px scab">
        <h4 class="t-orange mt-3">{{name}}</h4>
        <h5 class="t-orange my-4">{{price.pre}},<span class="font-14px">{{price.post}}/mês</span></h5>
       
        <p class="t-gray font-14px my-0" v-for="(b, idx) in benefits" :key="idx">{{b}}</p>

        <span class="">
            {{comment}}
        </span>

        <button class="btn btn-info px-4 mx-0 mt-5">Adquirir</button>
    </div>
</template>

<script>
    module.exports = {
        data: function () {
            return {}
        },
        props: {
            name: String,
            pic: String,
            comment: String, 
            benefits: Array, 
            price:{
                pre: String,
                post: String
            }
        },
        created:function(){
        }
    }
</script>

<style scooped>
    ul li{
        text-decoration: none;
        list-style-type: none;
    }
    .scab{
        border: 1px #FFE8AD solid;
    }
</style>