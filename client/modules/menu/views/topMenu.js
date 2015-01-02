define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
    	tpl      = require('text!menu/tpl/topMenu.html'),
        template = _.template(tpl);

    return Backbone.View.extend({

        render: function () {
            this.$el.html(template(this.model.attributes.top));
            return this;
        }

    });

});