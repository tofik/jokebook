# Create your views here.
from django.shortcuts import render_to_response
from jokebook.book.models import Joke

from book.models import *
from jokebook.book.forms import NewJokeForm

def new(request):
    form = NewJokeForm()
    return render_to_response('book/new.html',{'form': form})

def details(request):
    return render_to_response('book/details.html')

def list(request):
    all_jokes = Joke.objects.all().order_by('-created')
    return render_to_response('book/list.html', {'all_jokes': all_jokes})
