define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('pagesNew/models/model');

    return Backbone.View.extend({

        render: function () {
            var newPage = new model.NewPage();
            newPage.save({}, {
                    success: function (data) {
                        if (data.status === 1)
                            console.log(data.msg);
                        else
                            console.log(data.attributes);
                            document.router.navigate("pages/page/" + data.attributes.newPage, {trigger: true,  replace: true});
                    },
                    error: function (data) {
                        console.log(data);
                    }
            });

            return this;
        }

    });

});