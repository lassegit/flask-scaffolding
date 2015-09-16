# Flask Scaffolding with Python 3.4, BackboneJS/requireJS and Sass

## Install
Clone the repository and run:

````
bower install

npm install

make env
````

## Run
````
make dev or make prod
````

## Develop
The following command auto generates various Backbone MVC:
````
yo backbone:model blog
yo backbone:collection blog
yo backbone:router blog
yo backbone:view blog

````

This is taken from Yeoman.io's BackboneJS project.


## Deploy
Run `grunt build`.

## More
Set up uwsgi for production: https://github.com/mking/flask-uwsgi
