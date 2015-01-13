define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('pagesNotebooks/models/model'),
        NotebookView    = require('pagesNotebooks/views/notebook'),
        tpl      = require('text!pagesNotebooks/tpl/notebooks.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        render: function (menuView, id) {
            if (menuView) {
                menuView.updateMenu(model.MenuData);
            }

            this.$el.html(template());

            var notebooks = new model.Notebooks();
            if (id)
                notebooks.url = notebooks.url + id + '/';
            notebooks.fetch({
                    success: function (data) {
                        $('.notebooksModule').html('');
                        notebooks.each(function(notebook) {
                            // console.log(notebook.attributes);
                            $('.notebooksModule').append(new NotebookView({model: notebook}).render().el);
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