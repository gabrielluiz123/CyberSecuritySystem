<template>
    <div class="client-scrap lazy showcase col-12 col-sm-4">
        <img class="round lazy" :data-src="pic">
        <h4>{{name}}</h4>
        <p>{{comment}}</p>
        <i class="fas t-orange fa-gavel"></i>
        <i class="fas t-orange fa-gavel"></i>
        <i class="fas t-orange fa-gavel"></i>
        <i class="fas t-orange fa-gavel"></i>
        <i class="fas t-orange fa-gavel"></i>
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