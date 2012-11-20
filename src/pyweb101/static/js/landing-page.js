define(['jquery', 'underscore', 'backbone'],
    function(){
        var InputForm = Backbone.Model.extend({
            url: '/api/langinghypothesis/',
            defaults: {
                'email': ''
            },
            validate: function(attrs) {
                var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
                if (reg.test(attrs.email) == false){
                    return 'Invalid email';
                }
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
                this.model.set('email', $('input[type=text]').val());
                if (this.model.isValid()){
                    this.model.save();
                }

                return false;
            },
            validateData: function(){
                // TODO write validation method, dicide if it should be in model attribute change or 
                // in view
                return false;
            
            }
        });
        model = new InputForm();
        item = new InputView({model: model});
    }
);