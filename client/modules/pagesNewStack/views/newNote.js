define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('notesNew/models/model');

    return Backbone.View.extend({

        render: function () {
            var newNote = new model.NewNote();
            newNote.save({}, {
                    success: function (data) {
                        if (data.status === 1)
                            console.log(data.msg);
                        else
                            console.log(data.attributes);
                            document.router.navigate("notes/note/" + data.attributes.newNote, {trigger: true,  replace: true});
                    },
                    error: function (data) {
                        console.log(data);
                    }
            });

            return this;
        }

    });

});