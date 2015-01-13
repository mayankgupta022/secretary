define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('pagesNewStack/models/model');

    return Backbone.View.extend({

        render: function () {
            var newStack = new model.NewStack();
            newStack.save({}, {
                    success: function (data) {
                        if (data.status === 1)
                            console.log(data.msg);
                        else
                            console.log(data.attributes);
                            document.router.navigate("pages/stack/" + data.attributes.newStack, {trigger: true,  replace: true});
                    },
                    error: function (data) {
                        console.log(data);
                    }
            });

            return this;
        }

    });

});