import planBox from './vue.components/plan.vue'
let planData = {
    plans: [
        {
            name: "Gratis*",
            val : "00,00",
            benefits: [
                'Beneficio 1',
                'Benefício 2',
                'Benefício 3',
                'Benefício 4'
            ]
        },
        {
            name: "Pessoal*",
            val : "129,90",
            benefits: [
                'Beneficio 1',
                'Benefício 2',
                'Benefício 3',
                'Benefício 4'
            ]
        },
        {
            name: "Escritório*",
            val : "89,90*",
            benefits: [
                'Beneficio 1',
                'Benefício 2',
                'Benefício 3',
                'Benefício 4'
            ]
        },
    ]
}

var pls = new Vue({
    el: "#plans",
    data: planData,
    components:{
        planBox: planBox
    },
    methods: {

    },
    created:{

    }
})