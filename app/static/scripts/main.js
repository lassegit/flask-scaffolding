/*global require*/
'use strict';
require.config({
    shim: {
        handlebars: {
            exports: 'Handlebars'
        },
        bootstrap: { 
            deps:['jquery'],
            exports: '$.fn.boostrap'
        },
    },
    paths: {
        jquery: '../bower_components/jquery/dist/jquery',
        backbone: '../bower_components/backbone/backbone',
        underscore: '../bower_components/lodash/lodash',
        handlebars: '../bower_components/handlebars/handlebars',
        bootstrap: '../bower_components/bootstrap-sass/assets/javascripts/bootstrap',
    }
});

require([
    'jquery', 'underscore', 'backbone', 'templates', 'bootstrap', 'helpers', 'util',
], function ($, _, Backbone, JST, Bootstrap, Helpers, Util) {

    window.app = {
        views: {},
        models: {},
        collections: {}
    };

    var Router = Backbone.Router.extend({
        routes: {
            '': 'index',
            'user': 'user',
        },
        
        initialize: function() {
            $('[data-toggle="tooltip"]').tooltip(); // Run Bootstrap's tooltip
        },

        index: function() {},

        user: function() {},
    });

    window.Router = new Router();
    Backbone.history.start({pushState:true});

    $.ajaxSetup({
        headers: {
            'X-CSRF-Token': $('meta[name="csrf-token"]').attr('content') // CSRF for AJAX
        }
    });
});
