# Django Projects - Q19 & Q20

## Step 1: Create Virtual Environment

```bash
cd e:\Study\Study_test\Practical exercises Python
python -m venv venv
```

## Step 2: Activate Virtual Environment

```bash
.\venv\Scripts\Activate.ps1
```

## Step 3: Install Django

```bash
pip install django
```

## Step 4: Create Django Project

```bash
django-admin startproject myproject
```

## Step 5: Create App

```bash
python manage.py startapp myapp
```

## Step 6: Update settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Add this
]
```

## Step 7: Create views.py

File: `myapp/views.py`

```python
from django.shortcuts import render

def home(request):
    context = {'title': 'Home', 'message': 'Welcome to Django'}
    return render(request, 'myapp/index.html', context)

def about(request):
    context = {'title': 'About', 'message': 'About Page'}
    return render(request, 'myapp/about.html', context)
```

## Step 8: Create myapp/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

## Step 9: Update myproject/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

## Step 10: Create Templates Folder

```bash
mkdir myapp\templates\myapp
```

## Step 11: Create index.html

File: `myapp/templates/myapp/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    <a href="/">Home</a> | <a href="/about/">About</a>
</body>
</html>
```

## Step 12: Create about.html

File: `myapp/templates/myapp/about.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    <a href="/">Home</a> | <a href="/about/">About</a>
</body>
</html>
```

## Step 13: Run Migrations

```bash
python manage.py migrate
```

## Step 14: Run Server

```bash
python manage.py runserver
```

## Step 15: Open Browser

```
http://127.0.0.1:8000/
http://127.0.0.1:8000/about/
```


