define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        RestorePage = Backbone.Model.extend({
            urlRoot : document.serverURL + 'pages/restorePage/'
            });

    return {
        RestorePage: RestorePage
    };


});