define(function (require) {

    "use strict";

    var model       = require('common/models/model'),
        ShellView   = require('shell/views/shell'),
        MenuView    = require('menu/views/menu'),
        $body       = $('body'),
        shellView,
        menuView,
        currentView,
        $content;

    return Backbone.Router.extend({

        routes: {
            "": "home",
            "blank": "blank",
            "changePass": "changePass",
            "login": "login",
            "signUp": "signUp",
            "try/:id": "try"
        },

        initialize: function () {

            this.listenTo(this, "route", this.getInfo);

            shellView = new ShellView();
            $body.html(shellView.render().el);
            $content = $("#content");
            menuView = new MenuView({el: $content});
        },

        blank: function () {
            document.router.navigate("", {trigger: true, replace: true});//replace: true required if history not to be maintained
        },

        home: function () {
            var self = this;
            require(["home/views/home"], function (HomeView) {
                var homeView = new HomeView();
                self.updateCurrentView(homeView);
                $(homeView.render(menuView).el).appendTo($content);
            });
        },

        changePass: function () {
            var self = this;
            require(["changePass/views/changePass"], function (ChangePassView) {
                var changePassView = new ChangePassView();
                self.updateCurrentView(changePassView);
                $(changePassView.render(menuView).el).appendTo($content);
            });
        },

        login: function () {
            var self = this;
            require(["login/views/login"], function (LoginView) {
                var loginView = new LoginView();
                self.updateCurrentView(loginView);
                $(loginView.render(menuView).el).appendTo($content);
            });
        },

        signUp: function () {
            var self = this;
            require(["signUp/views/signUp"], function (SignUpView) {
                var signUpView = new SignUpView();
                self.updateCurrentView(signUpView);
                $(signUpView.render(menuView).el).appendTo($content);
            });
        },


        try: function (id) {
            console.log(id);
        },

        getInfo: function() {
            var getInfo = new model.GetInfo();
            getInfo.fetch({
                        success: function (data) {
                            document.user = data.user;
                            document.firstName = data.firstName;
                            document.lastName = data.lastName;
                            document.email = data.email;
                            document.role = data.role;
                        },
                        error: function (data) {
                            document.user = 'anon';
                            document.firstName = 'Anon';
                            document.lastName = '';
                            document.role = 0;
                        }
                });
        },

        updateCurrentView: function(newView) {
            //COMPLETELY UNBIND THE VIEW
            if(this.currentView) {
                this.currentView.undelegateEvents();
                $(this.currentView.el).removeData().unbind(); 
                //Remove currentView from DOM
                this.currentView.remove();  
                Backbone.View.prototype.remove.call(this.currentView);

            }
            this.currentView=newView;
            this.currentView.delegateEvents(); // delegate events when the view is recycled
        }

    });

});