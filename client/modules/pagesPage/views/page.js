define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('pagesPage/models/model'),
        tpl      = require('text!pagesPage/tpl/page.html'),
        page,
        readyToUpdate,

        template = _.template(tpl);

    return Backbone.View.extend({

        events: {
            "click #submit" : "page",
            "keydown" : "onkeydown",
            "change #pageName": "updatePage",
            "change #pageContent": "updatePage"
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

        updatePage: function() {
            var self = this;

            var name = $('#pageName').val(),
                priority = 0,
            //  attr1
            //  attr2
                content = $('#pageContent').val();

            self.page.save({
                    name: name,
                    priority: priority,
                    // attr1: attr1,
                    // attr2: attr2,
                    content: content
                    }, {
                        success: function (data) {
                            console.log(self.page.attributes);
                        },
                        error: function (data) {
                            console.log(data);
                        }
                });

            self.readyToUpdate = 0;
        },

        refresh: function() {
            var self = this;
            this.page.fetch({
                    success: function (data) {
                        console.log(data.attributes);            
                        self.$el.html(template(data.attributes.page));
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
            self.page =new model.Page();
            self.page.urlRoot = self.page.urlRoot + id + '/';
            self.refresh();
            self.readyToUpdate = 0;
            setInterval(function(){
                console.log(self.readyToUpdate);
                if (self.readyToUpdate) {
                    self.updatePage();
                } 
            }, 5000);

            return this;
        }

    });

});