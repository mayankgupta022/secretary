define(function (require) {

    "use strict";

    var Backbone = require('backbone'),

        DelEvent = Backbone.Model.extend({
            urlRoot : document.serverURL + 'diary/delEvent/'
            });

    return {
        DelEvent: DelEvent
    };


});