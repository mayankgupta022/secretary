define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('pagesDelStack/models/model');

    return Backbone.View.extend({

        render: function (id) {
            var delStack = new model.DelStack();
            delStack.urlRoot = delStack.urlRoot + id + "/";
            delStack.save({}, {
                    success: function (data) {
                        if (data.status === 1)
                            console.log(data.msg);
                        else
                            console.log(data.attributes);
                            document.router.navigate("pages", {trigger: true,  replace: true});
                    },
                    error: function (data) {
                        console.log(data);
                    }
            });

            return this;
        }

    });

});