define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        DelNotebook = Backbone.Model.extend({
            urlRoot : document.serverURL + 'pages/delNotebook/'
            });

    return {
        DelNotebook: DelNotebook
    };


});