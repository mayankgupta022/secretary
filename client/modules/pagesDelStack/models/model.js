define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        DelStack = Backbone.Model.extend({
            urlRoot : document.serverURL + 'pages/delStack/'
            });

    return {
        DelStack: DelStack
    };


});