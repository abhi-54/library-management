from django.shortcuts import render, redirect
from django import forms
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required

def admin_signup(request):
  form = myAdminForm()
  context = {
    'form': form
  }
  if request.POST:
    msg = ''
    form = myAdminForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        return redirect('admin-login')
      except forms.ValidationError:
        msg += '\n This email address already exists. Did you forget your password?'
        context['msg'] = msg
    else:
      msg += 'Please correct the entered details!'
      context['msg'] = msg
  return render(request, 'signup.html', context)

def admin_login(request):
  if request.GET:
    form = adminLoginForm()
    context = {
      'form': form
    }
    return render(request, 'login.html', context)
  else:
    form = adminLoginForm(data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect("admin-dashboard")
    else:
      context = {
          "form": form
      }
      return render(request, "login.html", context=context)

def logout(request):
	logout(request)
	return redirect("Login")

@staff_member_required
def admin_dashboard(request):
  return render(request, 'main.html')
