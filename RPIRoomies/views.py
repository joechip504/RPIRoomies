from django.shortcuts import render
from RPIRoomies.models import Person
import random

# Create your views here.

def index(request):
    context = { 
    'user': request.user,
    'request': request
     }
    return render(request, 'index.html', context)

def find(request):
    """
    This is just a demo, so just show 5 random users from the database.
    """
    context = { 
        'user': request.user,
        'request': request,
         }
    
    if request.user.is_anonymous():
        context['people'] = []
    else:
        all_people = [p for p in Person.objects.all() if (
                p.first_name != request.user.first_name and
                p.last_name != request.user.last_name)]

        context['people'] = random.sample(all_people, 5)

    return render(request, 'find.html', context)
