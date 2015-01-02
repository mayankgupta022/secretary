define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        menuData = {
            "top" : {
                "visible" : true,
                "left" : {
                    "visible" : true,
                    "title" : "topLeft",
                    "icon" : "",
                    "route" : "try/2",
                    "active" : false
                },
                "middle" : {
                    "visible" : true,
                    "title" : "Home",
                    "icon" : "",
                    "route" : "blank",
                    "active" : false
                },
                "right" : {
                    "visible" : true,
                    "title" : "topRight",
                    "icon" : "",
                    "route" : "",
                    "active" : false
                }
            },
            "bottom" : {
                "visible" : true,
                "first" : {
                    "visible" : true,
                    "title" : "bottomLeft",
                    "icon" : "",
                    "route" : "",
                    "active" : false
                },
                "second" : {
                    "visible" : true,
                    "title" : "bottomMiddle",
                    "icon" : "",
                    "route" : "",
                    "active" : false
                },
                "third" : {
                    "visible" : true,
                    "title" : "bottomRight",
                    "icon" : "",
                    "route" : "",
                    "active" : true
                }
            }
        },

        Login = Backbone.Model.extend({
            urlRoot : document.serverURL + 'user'
            });

    return {
        MenuData: menuData,
        Login: Login
    };


});