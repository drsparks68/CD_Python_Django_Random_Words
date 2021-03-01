from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    request.session['new_word'] = get_random_string(length=24)
    return render(request, 'index.html')

def reset(request):
    request.session['counter'] = 0
    return redirect('/random_word')
# Create your views here.
