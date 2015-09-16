define([
    'jquery',
    'underscore',
    'backbone',
    'templates',
], function ($, _, Backbone, JST) {
    'use strict';
    // If equals cheating helper
    Handlebars.registerHelper('equal', function(lvalue, rvalue, options) {
        if (arguments.length < 3)
            throw new Error("Handlebars Helper equal needs 2 parameters");
        if (lvalue != rvalue) {
            return options.inverse(this);
        } else {
            return options.fn(this);
        }
    });

    // If modulus return true
    Handlebars.registerHelper('ifmodulus', function(value, modulus, options) {
        if (parseInt(value) % parseInt(modulus) === 0) {
            return options.fn(this);
        }
        return options.inverse(this);
    });

    // Line break
    Handlebars.registerHelper('breaklines', function(text) {
        text = Handlebars.Utils.escapeExpression(text);
        text = text.replace(
            /((https?\:\/\/)|(www\.))(\S+)(\w{2,4})(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/gi,
            function(url) {
                var full_url = url;
                if (!full_url.match('^https?:\/\/')) {
                    full_url = 'http://' + full_url;
                }

                url = url.replace('http://', '').replace('https://', '').replace('www.', '');

                return '<a href="' + full_url + '" target="_blank">' + url + '</a>';
            }
        );
        text = text.replace(/(\r\n|\n|\r)/gm, '<br>');
        return new Handlebars.SafeString(text);
    });
});
