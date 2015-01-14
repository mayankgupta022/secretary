define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        tpl      = require('text!diaryEvents/tpl/event.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        render: function () {
            console.log(this.model.attributes.active);
            this.$el.html(template(this.model.attributes));
            return this;
        }

    });

});