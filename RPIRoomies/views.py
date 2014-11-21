from django.shortcuts import render

# Create your views here.

def index(request):
    context = { 
    'user': request.user,
    'request': request
     }
    return render(request, 'index.html', context)
