define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        tpl      = require('text!notes/tpl/note.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        render: function () {
            this.$el.html(template(this.model.attributes));
            return this;
        }

    });

});