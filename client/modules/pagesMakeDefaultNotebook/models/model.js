define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        MakeDefaultNotebook = Backbone.Model.extend({
            urlRoot : document.serverURL + 'pages/makeDefaultNotebook/'
            });

    return {
        MakeDefaultNotebook: MakeDefaultNotebook
    };


});