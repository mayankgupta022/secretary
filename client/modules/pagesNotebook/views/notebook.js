define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('pagesNotebook/models/model'),
        PageView = require('pages/views/page'),
        tpl      = require('text!pagesNotebook/tpl/notebook.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        render: function (menuView, id) {
            var self = this;

            if (menuView) {
                menuView.updateMenu(model.MenuData);
            }

            var notebook = new model.Notebook();
            if (id)
                notebook.urlRoot = notebook.urlRoot + id + '/';
            notebook.fetch({
                    success: function (data) {
                        self.$el.html(template(notebook.attributes.notebook));
                        $('#notebookMsg').html('');

                        console.log(notebook);
                        for (var page = 0; page < notebook.attributes.childPages.length ; page++) {
                            notebook.attributes.childPages[page].attributes = notebook.attributes.childPages[page];
                            $('#notebookMsg').append(new PageView({model: notebook.attributes.childPages[page]}).render().el);
                        };
                    },
                    error: function (data) {
                        console.log("data");
                    }
            });

            return this;
        }

    });

});