define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('diaryDelEvent/models/model');

    return Backbone.View.extend({

        render: function (id) {
            var delEvent = new model.DelEvent();
            delEvent.urlRoot = delEvent.urlRoot + id + "/";
            delEvent.save({}, {
                    success: function (data) {
                        if (data.status === 1)
                            console.log(data.msg);
                        else
                            console.log(data.attributes);
                            document.router.navigate("diary", {trigger: true,  replace: true});
                    },
                    error: function (data) {
                        console.log(data);
                    }
            });

            return this;
        }

    });

});