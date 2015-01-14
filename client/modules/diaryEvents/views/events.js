define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('diaryEvents/models/model'),
        NoteView    = require('diaryEvents/views/event'),
        tpl      = require('text!diaryEvents/tpl/events.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        render: function (menuView, id) {
            if (menuView) {
                menuView.updateMenu(model.MenuData);
            }

            this.$el.html(template());

            var events = new model.Events();
            if (id)
                events.url = events.url + id + '/';
            events.fetch({
                    success: function (data) {
                        $('.eventsModule').html('');
                        events.each(function(event) {
                            // console.log(event.attributes);
                            $('.eventsModule').append(new NoteView({model: event}).render().el);
                        });
                    },
                    error: function (data) {
                        console.log("data");
                    }
            });

            return this;
        }

    });

});