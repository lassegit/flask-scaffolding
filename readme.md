# Flask Scaffolding with Python 3.4, BackboneJS/requireJS, Bootstrap and Sass (libsass)

It contains OAuth logic for Google and Facebook, just fill in the missing keys in `app/controllers/authorize.py`. And also regular form login in `app/controllers/auth`.
   

## Install
Clone the repository `git clone https://github.com/lassecph/flask-scaffolding.git your_project_name` and `rm -r .git` folder. Fill out the needed settings in `app/settings.py`.

````
bower install

npm install

virtualenv -p /usr/local/bin/python3 venv (path to your python 3 installation)

. venv/bin/activate

make deps

./manage createdb

./manage server (or run uwsgi --ini uwsgi.ini --py-autoreload 1)

grunt watch (grunt build)

````

## Run
````
make dev or make prod (check commands in Makefile)
````

## Develop
The following command auto generates various Backbone MVC:
````
yo backbone:model blog
yo backbone:collection blog
yo backbone:router blog
yo backbone:view blog
````

This is taken from [Yeoman.io's BackboneJS project](https://github.com/yeoman/generator-backbone).


## Deploy
Run `grunt build`.

## More
Set up uwsgi for production: https://github.com/mking/flask-uwsgi

## Credits
Build on top of https://github.com/JackStouffer/Flask-Foundation

With the BackboneJS frontend from https://github.com/yeoman/generator-backbone

## Readmore
Flask documentation: http://flask.pocoo.org/docs/0.10/

Flask SQLAlchemy documentation: https://pythonhosted.org/Flask-SQLAlchemy/index.html

Flask Cache documentation: https://pythonhosted.org/Flask-Cache/

Flask Oauthlib documentation: https://flask-oauthlib.readthedocs.org/en/latest/
