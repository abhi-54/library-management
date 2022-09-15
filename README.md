# Library Management
Short overview of Django rest framework &amp; api
## General
* install requirements.txt </br>
```pip install -r requirements.txt```
* Note that mysql database is used, therefore, after configuring database, populate it with Book objects

<hr>
<hr>

## api/
### api/serializers.py
initialize the Book model with a serializer

### api/views.py
contains view based functions for APIs

<hr>
<hr>

## library_app/
### library_app/models.py
contains Book Model

## library_management/
django source folder containing settings.py

<hr>
<hr>

## myadmin/
### forms.py
* `myAdminForm()` module (Admin Sign Up form): 
    * inherits from django's UserCreationForm
    * makes 'email' as a required field
    * overrides `save()` method to implement 'admin' status to User
    </br>
* `adminLoginForm()` module (Admin Login form):
    * inherits from django's AuthenticationForm
    * sets `username` as `EmailField` 
    
