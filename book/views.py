import datetime
from django.shortcuts import render_to_response, HttpResponseRedirect, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from book.models import Joke
from book.models import *
from book.forms import NewJokeForm

def new(request):

    #save new joke
    if request.method == 'POST':
        form = NewJokeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book/list/')

    #or show clean form
    else:
        form = NewJokeForm()

    return render_to_response('book/new.html',{'form': form})

def details(request, joke):

    #fetch joke to display details for
    joke_for_details = get_object_or_404(Joke,pk=joke)

    #try to check whether there are prev and next
    prev = int(joke) - 1 #index for previous joke
    next = int(joke) + 1 #index for next joke
 
    try:
        previous_joke = Joke.objects.get(id=prev)
    except Joke.DoesNotExist:
        previous_joke = joke_for_details #if there is no previous, set current

    try:
        next_joke = Joke.objects.get(id=next)
    except Joke.DoesNotExist:
        next_joke = joke_for_details #if there is no next, set current
   
    
    return render_to_response('book/details.html', {'joke_for_details': joke_for_details, 
                                                    'next_joke':next_joke,
                                                    'previous_joke':previous_joke})

def list(request,order = 'created'):

    #order selection
    if order == 'top':
        all_jokes = Joke.objects.all().order_by('-rank')        
    #defualt order is from the latest to the oldest
    else:
        all_jokes = Joke.objects.all().order_by('-created')
 
    #pagination
    paginator = Paginator(all_jokes, 3)
    
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        jokes = paginator.page(page)
    except (EmptyPage, InvalidPage):
        jokes = paginator.page(paginator.num_pages)

    return render_to_response('book/list.html', {'jokes': jokes})

def vote(request,direction,joke_id):
    
    #simple session protection to avoid double voting by the same user
    if request.session.get('voted'+joke_id, False):
        return list(request)

    # vote in plus - each vote means one point
    if direction == 'plus':

        try:
            joke_obj = Joke.objects.get(id = joke_id)
            joke_obj.votes = joke_obj.votes + 1
            joke_obj.rank = joke_obj.rank + 1
            joke_obj.save()
            request.session['voted'+joke_id] = True        
        except Joke.DoesNotExist:
            print "No object!"

    #vote in minus - each vote means one point
    elif direction == 'minus':

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

def top(request):
    #returns the best jokes first
    return list(request,'top')


    
