from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response

from .services import get_items,  grab_item

# Create your views here.


def home(request):
    items = get_items()
    response = {}
    response['items'] = items
    return render_to_response('home.html', {'response': response})


def login(request):
    response = {}
    return render_to_response('login.html', {'response': response})


def peasant(request):
    response = {}
    return render_to_response('peasant.html', {'response': response})


def worthy(request):
    response = {}
    return render_to_response('worthy.html', {'response': response})


def grab(request, item_id):
    uuid = item_id
    if grab_item(uuid):
        return HttpResponse('True')
    else:
        return HttpResponse('False')