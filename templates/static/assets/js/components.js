var data = {

}

new Vue({
    el: "#vueExample",
    data: data,

    methods: {
        callSuccess: function(){
            return simpleAlert.show({
                message: 'Este é o alerta de Sucesso!',
                type: 'success'
            });
        },
        callWarning: function(){
            return simpleAlert.show({
                message: 'Este é o alerta de Aviso!',
                type: 'warn'
            });
        },
        callDanger: function(){
            return simpleAlert.show({
                message: 'Este é o alerta de Erro!',
                type: 'danger'
            });
        }
    }
});

new Vue({
    el: '#customAlert',
    data: {
        options:{
            message: 'Este é um alerta customizado!', 
            type: 'bg-grey', 
            icon: 'fa-angry',
            fontColor: 't-black',
            dismissable: false,
            ttl: 5000,
            gloss: {
                in: 'cubic-bezier(.54,.3,.39,1.58)',
                out: 'ease-out'
            }
        }
    },

    methods: {
        callCustomBtn: function(){
            return simpleAlert.show(this.options)
        },
        resize: function(event){
            console.log(event.target);
            var w = event.target.value.length*9;
            $(event.target).css('width', w);
            console.log(w);
        },
    },
});