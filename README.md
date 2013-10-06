django-app-template
===================

This is a django reuasable app's template. It uses the template feature in Django >= 1.4.


How to use::
-----------------------------------

    # Install Django
    pip install django>=1.4
    # Clone the repo
    git clone https://github.com/benzid-wael/django-app-template.git
    # Use the template
    django-admin.py startapp --template=django-app-template/template --extension=py,rst,in <app_name>


Generated files::
-----------------------------------

- README.rst - Some minor layout to get you started
- setup.py - A starting point for packaging your app
- MANIFEST.in - Includes your app templates and static resources
- AUTHORS - Add your name here
- LICENSE - Add a license here
- runtests.py - Simple helper for running the application tests
- tox.ini - Configured to run tests on Django 1.3/1.4/master on Python 2.6
- .gitignore/.hgignore - Just to save you a few key strokes

Also we generate an ``<app_name>`` directory that contains this files:
- ``<app_name>/__init__.py``
- ``<app_name>/models.py``
- ``<app_name>/urls.py``
- ``<app_name>/views.py``
- ``<app_name>/admin.py``



