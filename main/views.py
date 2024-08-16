from django.shortcuts import render
from user.models import User
from .parser import all_ctf

def index(request):
    user_activities = User.objects.order_by('-points')
    events = all_ctf()
    return render(request, 'index.html', {
        'user_activities': user_activities,
        'events': events,
    })
