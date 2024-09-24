# Django Tutorials

## Tutorial 1 - Requests and responses

* Start a Django project using the command `django-admin startproject <project-name>`

* Each Django project represents a full fledged web application. It consists of several components or modules called apps.

* Create a new app using `django-admin startapp <app-name>`

* These commands result in the following file structure:

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    polls/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
```

* The outer `mysite` folder is just a container - you can rename it to whatever.

* The inner `mysite` folder contains the main configuration details for the whole project.

* `manage.py` can be used to issue commands to Django to perform certain developer tasks.

* `polls` is a directory that represents a polls application for the mysite project.

* It has its own `admin.py` file - which is used to issue administrator tasks.

* `models.py` is used to define models (more on this later.)

* `views.py` is used to define views (more on this later.)

### Writing views

Views are special functions that are invoked when a certain HTTP request needs to be handled. 

* Typically, the client enters a URL in their browser. 

* The browser makes an HTTP request to the server.

* The server uses the Django framework to process this request - accepts the request, is directed to the correct view using the URL-configuration for a web app and then returns the necessary HTTP response.

* A view function must take at least one argument which represents the HTTP request.

* It must always return either an HTTP response or a 404 not found response.

### URLConfig

* URL configurations tell Django how to direct incoming traffic. Certain URLs must be handled by certain apps, and so on.

* Every app has its own URLConfig file.

* The `include` module is used to access URL configurations from other applications.

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")), # 
    path("admin/", admin.site.urls),
]
```

* This is how an application URL config would look like -

```python
# polls/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

Let's say a client goes to https://mysite.com/polls/

1. The root URL is handled by the mysite/urls.py configuration. It chops off everything that has matched up until now i.e. up until `/polls/` (excluding the domain name).

2. Then it sees that for anything that contains `polls/*` we must include the urls.py from the polls app and so it hands it over to `polls/urls.py`.

3. In `polls/urls.py` we basically get an empy string, which means that it must be handled by the first pattern in the list (remember that the first part of the URl has been chopped off by the previous level of URL resolution)


### `runserver`

Django comes with a built-in lightweight dev-server. Which means you can start up a server on your own machine. To get it up and running, issue `python manage.py runserver`.

# Database Setup

