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

Testing
-------

::

    git clone https://github.com/fivethreeo/django-netaxept.git
    cd django-netaxept
    virtualenv test_env
    source ./test_env/bin/activate
    pip install -r requirements.txt
    python runshell.py --merchantid [merchantid] --token [token]
    python runtests.py --merchantid [merchantid] --token [token]