from django.shortcuts import render
from .scripts.home import HomeView

def home(request):
    home = HomeView()
    langs = home.get_langs()
    bio = home.bio()
    social = home.socal_links()
    expertise = home.expertise()

    data = {
        'langs': langs,
        'bio': bio,
        'social': social,
        'expertise': expertise,
    }

    return(
        render(request, 'index.html', data)
    )
