define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        NewStack = Backbone.Model.extend({
            urlRoot : document.serverURL + 'pages/newStack/'
            });

    return {
        NewStack: NewStack
    };


});