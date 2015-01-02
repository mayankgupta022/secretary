define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        model    = require('login/models/model'),
        tpl      = require('text!login/tpl/login.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        events: {
            "click #submit" : "login",
            "keydown" : "onkeydown"
        },

        onkeydown: function(e) {
            var code = e.keyCode || e.which;
            if(code == 65) 
                this.login();
        },

        login: function() {

            var username = $('#username').val(),
                password = $('#password').val();
            if (username == '')
                $('#loginMsg').html('Please enter your username');
            else if (password == '')
                $('#loginMsg').html('Please enter your password');
            else {
                var login = new model.Login();
                login.save({//login.fetch({ data: $.param({ username: username}) });
                    username: username,
                    password: password
                    }, {
                        success: function (data) {
                            if (data.status === 1)
                                $('#loginMsg').html('Username and password do not match!');
                            else
                                document.router.navigate("blank", {trigger: true});
                        },
                        error: function (data) {
                            $('#loginMsg').html('Login failed');
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