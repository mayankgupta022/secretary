define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('pagesTrash/models/model'),
        PageView    = require('pages/views/page'),
        tpl      = require('text!pages/tpl/pages.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        render: function (menuView) {
            if (menuView) {
                menuView.updateMenu(model.MenuData);
            }

            this.$el.html(template());

            var trashPages = new model.TrashPages();
            trashPages.fetch({
                    success: function (data) {
                        $('.pagesModule').html('');
                        trashPages.each(function(page) {
                            // console.log(page.attributes);
                            $('.pagesModule').append(new PageView({model: page}).render().el);
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