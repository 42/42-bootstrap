42coffeecups.com team's django project template
===============================================

Batteries included
------------------

* HTML5 ready: <header>, <article>, <footer>
* CDN ready: custom storages can be easyly used because {% static path %} is used instead of {{STATIC_URL}}
* Makefile that makes running management commands a little easier: make run, make test, make migrate
* requirements.txt everything needed (pip-coompatible)
* base.html with blocks we use (block content, block header_content, block footer_content, block extra_style, block extra_head_js)
* Twitter bootstrap (less version)
* jquery 1.7.2 # TODO: update
* django-debug-toolbar
* sqlite3 as default DB
* fixture with user admin, password admin

Usage
-----
To use this template use next commands::
  
  git clone git@github.com:42/42-bootstrap.git
  PROJ_NAME=<newproject_name>
  django-admin.py startproject $PROJ_NAME --template=42-bootstrap --name='.gitignore,Makefile.def.buildbot,Makefile.def.default' --extension='json'
  cp Makefile.def.default Makefile.def
  cp $PROJ_NAME/settings/local.py.default $PROJ_NAME/settings/local.py
  pip install -r requirements.txt
  make syncdb
  make run

