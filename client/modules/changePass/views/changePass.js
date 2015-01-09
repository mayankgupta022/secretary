define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('changePass/models/model'),
        tpl      = require('text!changePass/tpl/changePass.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        events: {
            "click #submit" : "changePass",
            "keydown" : "onkeydown"
        },

        onkeydown: function(e) {
            var code = e.keyCode || e.which;
            var oldPassword = $('#oldPassword').val(),
                newPassword = $('#newPassword').val();
                confirmPassword = $('#confirmPassword').val();
            if (oldPassword != '')
                $('#oldPassword').removeClass('error').addClass('success');
            if (newPassword != '')
                $('#newPassword').removeClass('error').addClass('success');
            if (confirmPassword == newPassword)
                $('#confirmPassword').removeClass('error').addClass('success');
            else if (confirmPassword != '')
                $('#confirmPassword').removeClass('success').addClass('error');
            // if(code === 13) 
                // this.changePass();
        },

        changePass: function() {

            var oldPassword = $('#oldPassword').val(),
                newPassword = $('#newPassword').val();
                confirmPassword = $('#confirmPassword').val();
            if (oldPassword == '')
            {
                $('#changePassMsg').html('Please enter your old password');
                $('#oldPassword').removeClass('success').addClass('error').focus();
            }
            else if (newPassword == '')
            {
                $('#changePassMsg').html('Please enter your new password');
                $('#newPassword').removeClass('success').addClass('error').focus();
            }
            else if (confirmPassword == '')
            {
                $('#changePassMsg').html('  Please confirm your password');
                $('#confirmPassword').removeClass('success').addClass('error').focus();
            }
            else if (confirmPassword != newPassword)
            {
                $('#changePassMsg').html('New and Confirm passwords do not match. Please confirm your password');
                $('#confirmPassword').removeClass('success').addClass('error').focus();
            }
            else {
                var changePass = new model.ChangePass();
                changePass.save({
                    oldPassword: oldPassword,
                    newPassword: newPassword
                    }, {
                        success: function (data) {
                            if (data.attributes.status === 1 && data.attributes.msg === 'invalid')
                                $('#changePassMsg').html('You old password is incorrect!');
                            if (data.attributes.status === 1 && data.attributes.msg === 'deactivated')
                                $('#changePassMsg').html('Your account has been deactivated!');
                            else
                                document.router.navigate("blank", {trigger: true});
                        },
                        error: function (data) {
                            $('#changePassMsg').html('Changing Password failed');
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