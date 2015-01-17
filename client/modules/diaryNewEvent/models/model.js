define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        NewEvent = Backbone.Model.extend({
            urlRoot : document.serverURL + 'diary/newEvent/'
            });

    return {
        NewEvent: NewEvent
    };


});