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
            showErrorMessage: function(model, response){
                this.$('input[type=text]').css({'color': 'red'});
                this.$('input[type=text]').val('');
                this.$('input[type=text]').attr('placeholder', 'This email is used!');
                this.model.clear({'silent': true});
            },
            sendData: function(){
                this.model.set('email', $('input[type=text]').val());
                if (this.model.isValid() && this.model.isNew()){
                    this.model.save(this.model.toJSON(), {error: this.showErrorMessage});
                }

                return false;
            },
            validateData: function(){
                this.model.set('email', $('input[type=text]').val());
                this.render();
            }
        });
		
		

		// LandingPage
		LandingPageApp =  new (Backbone.Router.extend({
			routes: {
				 '': 'index',
				 'section/:section': 'renderSection'
			 },
			 initialize: function(){
 		        var model = new InputForm();
 		        var item = new InputView({model: model});
				
				// find all sections from dom and populate collection with them
				var sectionDOMs = $('.homeServ > li');
				sectionDOMs.each(function(index){
					var element = $(sectionDOMs[index])
					if (element.data('section')){
						// section = new SectionModel({'section': element.data('section')});
					}
				});
				
				// Prevent default actions clicking on section links
				// TODO update with view events
				var app = this;
			    $(document).on('click', 'a:not([data-bypass])', function (evt) {

			       var href = $(this).attr('href');
			       var protocol = this.protocol + '//';

			       if (href.slice(protocol.length) !== protocol) {
			         evt.preventDefault();
			         app.navigate(href, true);
			       }
			     }); //end
	
			 },
			 start: function(){
			 	Backbone.history.start({pushState: true});
			 },
			 index: function(){},
			 renderSection: function(section){
				 alert(section);
			 },
		})); //end

    }
);