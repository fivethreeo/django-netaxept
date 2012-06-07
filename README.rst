===============
django-netaxept
===============

A generic payment app for Django using Netaxept

Installation
------------

For the current stable version:

:: 
 
    pip install django-netaxept
    
For the development version:

::

    pip install -e git+git://github.com/fivethreeo/django-netaxept.git#egg=django-netaxept

Configuration
-------------

Add ``djnetaxept`` to ``settings.INSTALLED_APPS`` and run:

::

    manage.py syncdb

