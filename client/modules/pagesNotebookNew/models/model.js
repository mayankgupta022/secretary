define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        NewNote = Backbone.Model.extend({
            urlRoot : document.serverURL + 'notes/newNote/'
            });

    return {
        NewNote: NewNote
    };


});