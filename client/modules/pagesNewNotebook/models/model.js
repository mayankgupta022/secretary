define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        NewNotebook = Backbone.Model.extend({
            urlRoot : document.serverURL + 'pages/newNotebook/'
            });

    return {
        NewNotebook: NewNotebook
    };


});