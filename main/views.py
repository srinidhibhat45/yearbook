from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.



def index(request):
    people = User.objects.all()
    context = {
        'people': people
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def gallery(request):
    return render(request, 'main/gallery.html')
