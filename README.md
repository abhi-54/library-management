# Library Management
Short overview of Django rest framework &amp; api
## General
* install requirements.txt </br>
```pip install -r requirements.txt```
* Note that mysql database is used, therefore, after configuring database, populate it with Book objects

<hr>
<hr>

## api/
APIs to list all books; create, update and delete objects from Book model
### api/serializers.py
initialize the Book model with a serializer

### api/views.py
contains functions based views for APIs to 
   * display overview of API links 
   * list all objects from Book
   * create, update and delete objects from Book

<hr>
<hr>

## library_app/
### library_app/models.py
contains Book Model

<hr>
<hr>

## library_management/
django source folder containing settings.py

<hr>
<hr>

## myadmin/
Admin can create, update and delete objects from Book
### myadmin/forms.py
* `myAdminForm()` module (Admin Sign Up form): 
    * inherits from django's UserCreationForm
    * makes 'email' as a required field
    * overrides `save()` method to implement 'admin' status to User
    </br>
* `adminLoginForm()` module (Admin Login form):
    * inherits from django's AuthenticationForm
    * sets `username` as `EmailField` 

### myadmin/utils.py
* `EmailBackend()` module:
   * implements `authenticate()` method to authenticate using 'email' instead of django's default authentication using 'username' 
   
### myadmin/views.py
implements function based views for Admin - sign up, login & dashboard 

## student/
Student can only see all objects from Book
### student/forms.py
implements similar features as `myadmin/forms.py` to a student user 
* `studentSignUpForm()` module (Student Sign Up form): 
    * inherits from django's UserCreationForm
    * makes 'email' as a required field
    * overrides `save()` method to implement 'admin' status to User
    </br>
* `studentLoginForm()` module (Student Login form):
    * inherits from django's AuthenticationForm
    * sets `username` as `EmailField` 

### student/views.py
implements function based views for Student - sign up, login & dashboard
    
