import datetime
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

    if request.method == 'POST':
        form = NewJokeForm(request.POST)
        if form.is_valid():
            form.save()

    all_jokes = Joke.objects.all().order_by('-created')
    return render_to_response('book/list.html', {'all_jokes': all_jokes})

def vote_minus(request,joke_id):

    if request.session.get('voted'+joke_id, False):
        return list(request)

    try:
        joke_obj = Joke.objects.get(id = joke_id)
        joke_obj.votes = joke_obj.votes + 1
        if joke_obj.rank != 0:
            joke_obj.rank = joke_obj.rank - 1
        joke_obj.save()
        request.session['voted'+joke_id] = True        
    except Joke.DoesNotExist:
        print "No object!"
    
    return list(request)

def vote_plus(request,joke_id):

    if request.session.get('voted'+joke_id, False):
        return list(request)

    try:
        joke_obj = Joke.objects.get(id = joke_id)
        joke_obj.votes = joke_obj.votes + 1
        joke_obj.rank = joke_obj.rank + 1
        joke_obj.save()
        request.session['voted'+joke_id] = True        
    except Joke.DoesNotExist:
        print "No object!"
    
    return list(request)

def top(request):
    all_jokes = Joke.objects.all().order_by('-rank')
    return render_to_response('book/list.html', {'all_jokes': all_jokes})
    
