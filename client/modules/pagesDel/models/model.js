define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        DelPage = Backbone.Model.extend({
            urlRoot : document.serverURL + 'pages/delPage/'
            });

    return {
        DelPage: DelPage
    };


});