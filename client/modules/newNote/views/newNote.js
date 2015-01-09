define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('newNote/models/model');

    return Backbone.View.extend({

        render: function (menuView) {
            var newNote = new model.NewNote();
            newNote.save({}, {
                    success: function (data) {
                        if (data.status === 1)
                            console.log(data.msg);
                        else
                            console.log(data.attributes);
                            document.router.navigate("note/" + data.attributes.newNote, {trigger: true,  replace: true});
                    },
                    error: function (data) {
                        console.log(data);
                    }
            });

            return this;
        }

    });

});