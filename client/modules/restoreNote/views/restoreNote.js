define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('restoreNote/models/model');

    return Backbone.View.extend({

        render: function (id) {
            var restoreNote = new model.RestoreNote();
            restoreNote.urlRoot = restoreNote.urlRoot + id + "/";
            restoreNote.save({}, {
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