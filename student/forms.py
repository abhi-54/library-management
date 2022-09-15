from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class studentSignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=25, required=True)
  class Meta:
    model = User
    fields = [
      'first_name',
      'last_name',
      'username',
      'email',
      'password1',
      'password2',
    ]

  def save(self, commit=True):
    def clean(self):
      email = self.cleaned_data.get('email')
      if User.objects.filter(email=email).exists():
        raise forms.ValidationError("Email exists")
      return self.cleaned_data
    clean(self)
    user = super (studentSignUpForm , self ).save(commit=False)
    user.is_staff = False
    user.is_superuser = False
    if commit:
      user.save()
    return user

class studentLoginForm(AuthenticationForm):
  username = forms.EmailField(label='Email Address')

