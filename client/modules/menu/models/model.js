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
                    "route" : "",
                    "active" : false
                },
                "middle" : {
                    "visible" : true,
                    "title" : "topMiddle",
                    "icon" : "",
                    "route" : "",
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

    Menu =  new Backbone.Model(menuData);
    
    return {
        Menu: Menu
    };


});