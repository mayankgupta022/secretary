define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('pages/models/model'),
        NoteView    = require('pages/views/page'),
        tpl      = require('text!pages/tpl/pages.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        render: function (menuView, id) {
            if (menuView) {
                menuView.updateMenu(model.MenuData);
            }

            this.$el.html(template());

            var pages = new model.Pages();
            if (id)
                pages.url = pages.url + id + '/';
            pages.fetch({
                    success: function (data) {
                        $('.pagesModule').html('');
                        pages.each(function(page) {
                            // console.log(page.attributes);
                            $('.pagesModule').append(new NoteView({model: page}).render().el);
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