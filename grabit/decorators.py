from django.http import HttpResponseRedirect
from django.shortcuts import reverse, redirect
from django.urls import resolve


def find_worth(function):
    def _function(request, *args, **kwargs):
        if request.user.is_worthy:
            if resolve(request.path_info).url_name != reverse('worthy').replace('/', ''):
                return redirect(reverse('worthy'))
        elif not request.user.is_worthy:
            if resolve(request.path_info).url_name != reverse('peasant').replace('/', ''):
                return redirect(reverse('peasant'))
        return function(request, *args, **kwargs)
    return _function