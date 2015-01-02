define(function (require) {

    "use strict";

    var Backbone       = require('backbone'),
        model          = require('menu/models/model'),
        TopMenuView    = require('menu/views/topMenu'),
        BottomMenuView = require('menu/views/bottomMenu'),
        topMenuView,
        bottomMenuView;

    return Backbone.View.extend({

        initialize: function() {
            topMenuView = new TopMenuView({model: model.Menu, el: $('#topMenu')});
            bottomMenuView = new BottomMenuView({model: model.Menu, el: $('#bottomMenu')});
        },

        updateMenu: function(menuData) {
            model.Menu.attributes = menuData;
            this.render();
        },

        render: function () {
            topMenuView.render();
            bottomMenuView.render();
            return this;
        }

    });

});