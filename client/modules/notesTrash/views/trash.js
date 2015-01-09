define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('notesTrash/models/model'),
        NoteView    = require('notes/views/note'),
        tpl      = require('text!notes/tpl/notes.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        render: function (menuView) {
            if (menuView) {
                menuView.updateMenu(model.MenuData);
            }

            this.$el.html(template());

            var trashNotes = new model.TrashNotes();
            trashNotes.fetch({
                    success: function (data) {
                        $('.notesModule').html('');
                        trashNotes.each(function(note) {
                            // console.log(note.attributes);
                            $('.notesModule').append(new NoteView({model: note}).render().el);
                        });
                    },
                    error: function (data) {
                        console.log("data");
                    }
            });

            return this;
        }

    });

});