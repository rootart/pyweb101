define(['jquery', 'underscore', 'backbone', 'backbone-tastypie'],
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
				this.model.on('change', this.render, this);
            },
            events: {
                "click button[type=submit]": "sendData",
                "blur input[name=email]": "validateData",
            },
			render: function(){
				if (!this.model.isNew()){
					this.$el.html('<p>Thanks we will contact you soon!</p>');
					this.$el.addClass('success');
				}
				if (!this.model.isValid()){
					this.$('input[type=text]').css({'color': 'red'});
				}
				else {
					this.$('input[type=text]').css({'color': '#BBB'});
				}
			},
            sendData: function(){
                this.model.set('email', $('input[type=text]').val());
                if (this.model.isValid() && this.model.isNew()){
                    this.model.save();
                }

                return false;
            },
			validateData: function(){
				this.model.set('email', $('input[type=text]').val());
				this.render();
			}
        });
        var model = new InputForm();
        var item = new InputView({model: model});
    }
);