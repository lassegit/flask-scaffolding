define([
    'jquery',
    'underscore',
    'backbone',
    'templates',
], function ($, _, Backbone, JST) {
    Backbone.View.prototype.scrollTop = function() {
        $('html,body').animate({
            scrollTop: 0
        }, 250);
    }

    Backbone.View.prototype.setAlert = function (message, type) {
        if (!type) {
            type = 'danger';
        }
        
        var alert = [
            '<div class="alert alert-' + type + ' alert-dismissible">',
                '<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>',
                message,
            '</div>',
        ].join('\n');

        $('#alert-wrapper').html(alert);
    }
});
