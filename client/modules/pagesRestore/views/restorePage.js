define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('pagesRestore/models/model');

    return Backbone.View.extend({

        render: function (id) {
            var restorePage = new model.RestorePage();
            restorePage.urlRoot = restorePage.urlRoot + id + "/";
            restorePage.save({}, {
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