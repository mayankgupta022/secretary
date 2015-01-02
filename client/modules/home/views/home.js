define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('home/models/model'),
        tpl      = require('text!home/tpl/home.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        render: function (menuView) {
            if (menuView) {
                menuView.updateMenu(model.MenuData);
            }
            this.$el.html(template());
            return this;
        }

    });

});