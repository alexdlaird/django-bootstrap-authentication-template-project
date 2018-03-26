[![Build Status](https://travis-ci.org/alexdlaird/django-bootstrap-authentication-template-project.svg?branch=master)](https://travis-ci.org/alexdlaird/django-bootstrap-authentication-template-project)
[![codecov](https://codecov.io/gh/alexdlaird/django-bootstrap-authentication-template-project/branch/master/graph/badge.svg)](https://codecov.io/gh/alexdlaird/django-bootstrap-authentication-template-project)


Django Bootstrap/Authentication Template Project
================

## Prerequisites
* Python (>= 2.7, >= 3.6)
* Pip (>= 9.0)

## Getting Started
The project is developed using [Python](https://www.python.org/), [Django](https://www.djangoproject.com), and [Bootstrap](http://getbootstrap.com/docs/3.3/).

This repository contains the source code for a Django Bootstrap/Authentication Template Project.

### Project Setup
To setup the Python/Django build environment, execute:

```
make install
```

To ensure the database is in sync with the latest schema, database migrations are generated and run with Django. To run migrations, execute:

```
make migrate
```

Once migrations have been run, you can create a super user, which is a standard user that also has access to the /admin site.

```
python manage.py createsuperuser
```

Now you're all set! To start the development server, execute:

```
python manage.py runserver
```

A development server will be started at http://localhost:8000.