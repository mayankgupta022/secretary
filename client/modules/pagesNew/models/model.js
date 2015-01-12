define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        NewPage = Backbone.Model.extend({
            urlRoot : document.serverURL + 'pages/newPage/'
            });

    return {
        NewPage: NewPage
    };


});