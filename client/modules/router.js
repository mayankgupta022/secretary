define(function (require) {

    "use strict";

    var model       = require('common/models/model'),
        ShellView   = require('shell/views/shell'),
        MenuView    = require('menu/views/menu'),
        $body       = $('body'),
        shellView,
        menuView,
        $content;

    return Backbone.Router.extend({

        routes: {
            "": "home",
        },

        initialize: function () {
            shellView = new ShellView();
            $body.html(shellView.render().el);
            $content = $("#content");
            menuView = new MenuView({el: $content});
        },

        home: function () {
            // homeView.delegateEvents(); // delegate events when the view is recycled
            require(["home/views/home"], function (HomeView) {
                var homeView = new HomeView({el: $content});
                homeView.render(menuView);
            });
        }

    });

});