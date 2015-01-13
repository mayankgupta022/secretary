define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('pagesMakeDefaultNotebook/models/model');

    return Backbone.View.extend({

        render: function (id) {
            console.log(id);
            var makeDefaultNotebook = new model.MakeDefaultNotebook();
            makeDefaultNotebook.urlRoot = makeDefaultNotebook.urlRoot + id + "/";
            console.log(makeDefaultNotebook.urlRoot);
            makeDefaultNotebook.save({}, {
                    success: function (data) {
                        if (data.status === 1)
                            console.log(data.msg);
                        else
                            console.log(data.attributes);
                            document.router.navigate("pages/notebooks", {trigger: true,  replace: true});
                    },
                    error: function (data) {
                        console.log(data);
                    }
            });

            return this;
        }

    });

});