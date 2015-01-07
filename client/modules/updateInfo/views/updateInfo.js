define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('updateInfo/models/model'),
        tpl      = require('text!updateInfo/tpl/updateInfo.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        events: {
            "click #submit" : "updateInfo",
            "keydown" : "onkeydown"
        },

        onkeydown: function(e) {
            var code = e.keyCode || e.which;
            var firstName = $('#firstName').val(),
                lastName = $('#lastName').val();
            if (firstName != '')
                $('#firstName').removeClass('error').addClass('success');
            // if(code === 13) 
                // this.updateInfo();
        },

        updateInfo: function() {

            var firstName = $('#firstName').val(),
                lastName = $('#lastName').val();
            if (firstName == '')
            {
                $('#updateInfoMsg').html('Please enter your First Name');
                $('#firstName').removeClass('success').addClass('error').focus();
            }
            else {
                var updateInfo = new model.UpdateInfo();
                updateInfo.save({
                    firstName: firstName,
                    lastName: lastName
                    }, {
                        success: function (data) {
                            console.log("Info updated")
                        },
                        error: function (data) {
                            console.log("data");
                        }
                });
            }
        },

        render: function (menuView) {
            if (menuView) {
                menuView.updateMenu(model.MenuData);
            }
            this.$el.html(template());
            return this;
        }

    });

});