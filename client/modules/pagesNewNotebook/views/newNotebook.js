define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('pagesNewNotebook/models/model');

    return Backbone.View.extend({

        render: function () {
            var newNotebook = new model.NewNotebook();
            newNotebook.save({}, {
                    success: function (data) {
                        if (data.status === 1)
                            console.log(data.msg);
                        else
                            console.log(data.attributes);
                            document.router.navigate("pages/notebook/" + data.attributes.newNotebook, {trigger: true,  replace: true});
                    },
                    error: function (data) {
                        console.log(data);
                    }
            });

            return this;
        }

    });

});