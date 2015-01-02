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
            "login": "login",
            "try/:id": "try"
        },

        initialize: function () {
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

        login: function () {
            var self = this;
            require(["login/views/login"], function (LoginView) {
                var loginView = new LoginView();
                self.updateCurrentView(loginView);
                $(loginView.render(menuView).el).appendTo($content);
            });
        },

        try: function (id) {
            console.log(id);
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