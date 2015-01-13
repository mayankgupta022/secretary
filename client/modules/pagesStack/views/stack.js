define(function (require) {

    "use strict";

    var Backbone     = require('backbone'),
        model        = require('pagesStack/models/model'),
        NotebookView = require('pagesStack/views/notebook'),
        tpl          = require('text!pagesStack/tpl/stack.html'),

        template     = _.template(tpl);

    return Backbone.View.extend({

        render: function (menuView, id) {
            var self = this;

            if (menuView) {
                menuView.updateMenu(model.MenuData);
            }

            var stack = new model.Stack();
            if (id)
                stack.urlRoot = stack.urlRoot + id + '/';
            stack.fetch({
                    success: function (data) {
                        self.$el.html(template(stack.attributes.stack));
                        $('#stackMsg').html('');

                        console.log(stack);
                        for (var page = 0; page < stack.attributes.childNotebooks.length ; page++) {
                            stack.attributes.childNotebooks[page].attributes = stack.attributes.childNotebooks[page];
                            $('#stackMsg').append(new NotebookView({model: stack.attributes.childNotebooks[page]}).render().el);
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