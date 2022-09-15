from django.http import HttpResponse
from django.shortcuts import render

def test_view(request):
  return HttpResponse('<h1>Runned</h1>')
