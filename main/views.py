from django.shortcuts import render, HttpResponse

# Create your views here.

people = [
    {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    },
     {
        'name': 'Shri',
        'college': 'Goa College of Engineering',
        'team': 'Tejas',
        'quote': 'Do This and Do That, Life will follow with everything else. Be comfident and bold!!',
        'img': 'https://i.ibb.co/r0qV7PW/sophists-logo.png'
    }

]


def index(request):
    context = {
        'people': people
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def gallery(request):
    return render(request, 'main/gallery.html')


def join(request):
    return render(request, 'main/join.html')
