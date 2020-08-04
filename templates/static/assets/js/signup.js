var response;
var signUp = {
    execution: '',
    name: '',
    pwd: '',
    email:''
}

new Vue({
    el: '#signup',
    data: signUp,

    methods: {

        signUp: function(){

            if(this.name.length <=  0) return simpleAlert.show({message: 'Precisa preencher seu nome!'}); else
            if(this.email.length <= 0) return simpleAlert.show({message: 'Precisa preencher seu e-mail!'}); else
            if(this.pwd.length < 6) return simpleAlert.show({message: 'Sua senha necessita de ao menos 6 caractéres!'});
            
            else 
            {
                $.post('/api/usr/signup', signUp, null, 'json').then(function(r){
                    signUp.execution = 'login_execute';       
                    if(r.res != null){
                        response = {message: r.res, alertType: 'success'}; 
                            $.post('/api/usr/login', signUp, null, 'json').then(function(r){
                                 if(r.res != null) {
                                     response = {message: r.res, alertType: 'success'};
                                     $('#login_modal').modal('hide');
                                     $('#btnLogout').show();
                                     $('#btnLogin').hide();
                                 
                                    setTimeout(function(){
                                        location.href="/admin"
                                    },2000)

                                 }                        
                             });
                        
                        }else

                    if(r.err != null) response = {message: r.err, alertType: 'warn'};
                   
                    simpleAlert.show({
                        message: response.message,
                        type: response.alertType
                    });


                })
            }
        },

    },

    created: function(){

    }
});

