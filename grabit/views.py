from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render_to_response('home.html',{})

def login(request):
    response = {}
    return render_to_response('login.html', {'response':response})

def peasant(request):
    response = {}
    return render_to_response('peasant.html', {'response':response})

def worthy(request):
    response = {}
    return render_to_response('worthy.html', {'response':response})

