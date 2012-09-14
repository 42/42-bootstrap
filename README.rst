===============================================
42coffeecups.com team's django project template
===============================================

What and Why
============
This is django template for startproject management command. It solves next tasks:

* "make run", "make test", "make migrate" and other short usefull commands defined in Makefile.
* Standartized project and application structure. This is critical if there are many developers working on project.
* Extensible base.html that is flexible enough for almost all our projects. And it uses bootstrap flexible layout.
* helpers42cc reusable django application that will be filled with commonly used solutions. Right now it includes: userpic templatetag, resize_image helper and validate_resizable validator.
* Coming soon: Some commonly used solutions that depend on actual models will be placed in "demo" django application. These includes: haystack-solr searching, social auth, etc.


Batteries included
==================

* HTML5 ready: <header>, <article>, <footer>.
* CDN ready: custom storages can be easily used because {% static path %} is used instead of {{STATIC_URL}}.
* Makefile that makes running management commands a little easier: make run, make test, make migrate.
* requirements.txt with everything needed (pip-compatible).
* base.html with blocks we use (block content, block header_content, block extra_style, etc.). `More on templates`_.
* `Useful helpers`_
* Twitter bootstrap (less version). base.html uses one collumn fluid layout
* jquery 1.7.2  # TODO: update.
* django-debug-toolbar.
* sqlite3 as default DB.
* fixture with user admin, password admin.


Usage
=====
To use this template use next commands::
  
  git clone git@github.com:42/42-bootstrap.git
  PROJ_NAME=<newproject_name>
  django-admin.py startproject $PROJ_NAME --template=42-bootstrap --name='.gitignore,Makefile.def.buildbot,Makefile.def.default' --extension='json'
  cd $PROJ_NAME
  cp Makefile.def.default Makefile.def
  cp $PROJ_NAME/settings/local.py.default $PROJ_NAME/settings/local.py
  pip install -r requirements.txt
  make syncdb
  make run


To use app template::

  git clone git@github.com:42/42-bootstrap.git
  django-admin.py startapp APP_NAME --template 42-bootstrap/app_template/ 


More on templates
=================
Base template skeleton includes many blocks that often should be filled with custom content. It already uses bootstrap's one collumn fluid layout. New templates may look like this::
  
  {% extends 'base.html' %}  

  {% block extra_style %}
    <link rel="stylesheet/less" type="text/css" href="{% static 'css/otherpage.less' %}">
  {% endblock extra_style %}

  {% block extra_head_js %}
    <script type="text/javascript" src="{% static 'otherpage.js' %}"></script>
  {% endblock extra_head_js %}
  
  
  {% block header_content %}
   Header menu
  {% endblock header_content %}
  
  
  {% block content %}
    {% for item in item_list %}
      {{ item }}
    {% endfor %}
  {% endblock content %}

  {% block footer %}
    Custom footer
  {% endblock footer %}


Useful helpers
====================
Project includes reusable app helpers42cc. Include it in INSTALLED_APPS and use.


Template Tags
-------------
Right now there is only one template tag: userpic_for

userpic_for
~~~~~~~~~~~

When `django profiles`_ are used and they have image field for userpic this tag becomes handy::
  
  {% userpic for request.user %} {# will output <img> for full sized userpic#}
  {% userpic for request.user "40x40" %} {# will output <img> for userpic resized to 40x40#}

.. _django profiles: https://docs.djangoproject.com/en/1.4/topics/auth/#storing-additional-information-about-users


In settings you can configure image field name and path to noavatar image::
  
  HELP42CC_USERPIC_FIELD = 'userpic'
  HELP42CC_NOPIC_PATH = 'img/noavatar.png'


Validators
----------

validate_resizable(image) — checks that image can be resized with solr.thumbnail

Utils
-----
resize_image(image, size=(1920, 1200)) — resizes image to specific size
