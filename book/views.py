# Create your views here.
from django.shortcuts import render_to_response

from book.models import *

def new(request):
    return render_to_response('book/new.html')

def details(request):
    return render_to_response('book/details.html')

def list(request):
    return render_to_response('book/list.html')
