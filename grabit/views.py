from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, reverse, redirect
from .decorators import find_worth
from .services import get_items, grab_item

# Create your views here.


@find_worth
def home(request):
    items = get_items()
    response = {}
    response['items'] = items
    return render_to_response('home.html', {'response': response})


def login(request):
    response = {}
    if request.user.is_authenticated():
        return redirect(reverse('home'))
    return render_to_response('login.html', {'response': response})

@find_worth
def peasant(request):
    response = {}
    return render_to_response('peasant.html', {'response': response})


def worthy(request):
    response = {}
    return render_to_response('worthy.html', {'response': response})

def signup(request):
    response = {}
    return render_to_response('worthy.html', {'response': response})

def grab(request, item_id):
    uuid = item_id
    request.user.is_worthy = grab_item(uuid)
    request.user.save()
    return HttpResponseRedirect('/')