define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('diaryNewEvent/models/model');

    return Backbone.View.extend({

        render: function () {
            var newEvent = new model.NewEvent();
            newEvent.save({}, {
                    success: function (data) {
                        if (data.status === 1)
                            console.log(data.msg);
                        else
                            console.log(data.attributes);
                            document.router.navigate("diary/event/" + data.attributes.newEvent, {trigger: true,  replace: true});
                    },
                    error: function (data) {
                        console.log(data);
                    }
            });

            return this;
        }

    });

});