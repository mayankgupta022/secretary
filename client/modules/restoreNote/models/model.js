define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        RestoreNote = Backbone.Model.extend({
            urlRoot : document.serverURL + 'notes/restoreNote/'
            });

    return {
        RestoreNote: RestoreNote
    };


});