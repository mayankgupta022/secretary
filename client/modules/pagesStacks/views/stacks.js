define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('pagesStacks/models/model'),
        StackView    = require('pagesStacks/views/stack'),
        tpl      = require('text!pagesStacks/tpl/stacks.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        render: function (menuView, id) {
            if (menuView) {
                menuView.updateMenu(model.MenuData);
            }

            this.$el.html(template());

            var stacks = new model.Stacks();
            if (id)
                stacks.url = stacks.url + id + '/';
            stacks.fetch({
                    success: function (data) {
                        $('.stacksModule').html('');
                        stacks.each(function(stack) {
                            // console.log(stack.attributes);
                            $('.stacksModule').append(new StackView({model: stack}).render().el);
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