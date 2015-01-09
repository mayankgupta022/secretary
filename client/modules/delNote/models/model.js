define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        DelNote = Backbone.Model.extend({
            urlRoot : document.serverURL + 'notes/delNote/'
            });

    return {
        DelNote: DelNote
    };


});