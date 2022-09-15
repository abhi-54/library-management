from django.shortcuts import render, redirect
from django import forms
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def student_signup(request):
  form = studentSignUpForm()
  context = {
    'form': form
  }
  if request.POST:
    msg = ''
    form = studentSignUpForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        return redirect('student-login')
      except forms.ValidationError:
        msg += '\n This email address already exists. Did you forget your password?'
        context['msg'] = msg
    else:
      msg += 'Please correct the entered details!'
      context['msg'] = msg
  return render(request, 'signup.html', context)

def student_login(request):
  if request.GET:
    form = studentLoginForm()
    context = {
      'form': form
    }
    return render(request, 'login.html', context)
  else:
    form = studentLoginForm(data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect("student-dashboard")
    else:
      context = {
          "form": form
      }
      return render(request, "login.html", context=context)

def logout(request):
	logout(request)
	return redirect("login")

@login_required
def student_dashboard(request):
  return render(request, 'student.html')
