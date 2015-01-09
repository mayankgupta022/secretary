define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('delNote/models/model');

    return Backbone.View.extend({

        render: function (id) {
            var delNote = new model.DelNote();
            delNote.urlRoot = delNote.urlRoot + id + "/";
            delNote.save({}, {
                    success: function (data) {
                        if (data.status === 1)
                            console.log(data.msg);
                        else
                            console.log(data.attributes);
                            document.router.navigate("notes", {trigger: true,  replace: true});
                    },
                    error: function (data) {
                        console.log(data);
                    }
            });

            return this;
        }

    });

});