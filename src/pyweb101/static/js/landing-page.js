define(['jquery', 'underscore', 'backbone'],
    function(){
        var InputForm = Backbone.Model.extend({
            defaults: {
                'placeholder': 'Your e-mail',
                'email': ''
            }
        });

        var InputView = Backbone.View.extend({
            el: '.email-form',
            model: InputForm,
            initialize: function(){
        
            },
            events: {
                "click input[type=submit]": "sendData",
                "blur input[type=text]": "validateData",
            },
            sendData: function(){
                // alert('ok');
                this.model.set('email', $('input[type=text]').val());
                return false;
            },
            validateData: function(){
                alert('changing');
                return false;
            
            }
        });
        model = new InputForm();
        item = new InputView({model: model});
    }
);