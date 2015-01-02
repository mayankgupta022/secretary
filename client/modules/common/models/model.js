define(function (require) {

    "use strict";

    var Backbone  = require('backbone'),
        server_ip = 'localhost';

    document.serverURL = 'http://' . server_ip;
    document.mediaURL = 'http://' . server_ip;

     var originalSync = Backbone.sync;

    Backbone.sync = function (method, model, options) {
        if (method === "read") {
            options.dataType = "jsonp";
            return originalSync.apply(Backbone, arguments);
        }
    };

    return {
    };


});