define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('diaryEvent/models/model'),
        tpl      = require('text!diaryEvent/tpl/event.html'),
        event,
        readyToUpdate,

        template = _.template(tpl);

    return Backbone.View.extend({

        events: {
            "click #submit" : "event",
            "keydown" : "onkeydown",
            "change #eventName": "updateEvent",
            "change #eventContent": "updateEvent"
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

        updateEvent: function() {
            var self = this;

            var name = $('#eventName').val(),
                priority = 0,
            //  attr1
            //  attr2
                content = $('#eventContent').val();

            self.event.save({
                    name: name,
                    priority: priority,
                    // attr1: attr1,
                    // attr2: attr2,
                    content: content
                    }, {
                        success: function (data) {
                            console.log(self.event.attributes);
                        },
                        error: function (data) {
                            console.log(data);
                        }
                });

            self.readyToUpdate = 0;
        },

        refresh: function() {
            var self = this;
            this.event.fetch({
                    success: function (data) {
                        console.log(data.attributes);            
                        self.$el.html(template(data.attributes.event));
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
            self.event =new model.Event();
            self.event.urlRoot = self.event.urlRoot + id + '/';
            self.refresh();
            self.readyToUpdate = 0;
            setInterval(function(){
                console.log(self.readyToUpdate);
                if (self.readyToUpdate) {
                    self.updateEvent();
                } 
            }, 5000);

            return this;
        }

    });

});