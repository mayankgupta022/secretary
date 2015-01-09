define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('notesNote/models/model'),
        tpl      = require('text!notesNote/tpl/note.html'),
        note,
        readyToUpdate,

        template = _.template(tpl);

    return Backbone.View.extend({

        events: {
            "click #submit" : "note",
            "keydown" : "onkeydown",
            "change #noteName": "updateNote",
            "change #noteContent": "updateNote"
        },

        onkeydown: function(e) {
            var code = e.keyCode || e.which;
            // var username = $('#username').val(),
            //     password = $('#password').val();
            // if (username != '')
            //     $('#username').removeClass('error').addClass('success');
            // if (password != '')
            //     $('#password').removeClass('error').addClass('success');
            // if(code === 13) 
                //something
            this.readyToUpdate = 1;
        },

        updateNote: function() {
            var self = this;

            var name = $('#noteName').val(),
                priority = 0,
            //  attr1
            //  attr2
                content = $('#noteContent').val();

            self.note.save({
                    name: name,
                    priority: priority,
                    // attr1: attr1,
                    // attr2: attr2,
                    content: content
                    }, {
                        success: function (data) {
                            console.log(self.note.attributes);
                        },
                        error: function (data) {
                            console.log(data);
                        }
                });

            self.readyToUpdate = 0;
        },

        refresh: function() {
            var self = this;
            this.note.fetch({
                    success: function (data) {
                        console.log(data.attributes);            
                        self.$el.html(template(data.attributes.note));
                    },
                    error: function (data) {
                        console.log("data");
                    }
            });
        },

        render: function (menuView, id) {
            var self = this;

            if (menuView) {
                menuView.updateMenu(model.MenuData);
            }
            self.note =new model.Note();
            self.note.urlRoot = self.note.urlRoot + id + '/';
            self.refresh();
            self.readyToUpdate = 0;
            setInterval(function(){
                console.log(self.readyToUpdate);
                if (self.readyToUpdate) {
                    self.updateNote();
                } 
            }, 5000);

            return this;
        }

    });

});