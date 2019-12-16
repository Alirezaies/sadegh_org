from django.shortcuts import render
from .scripts.home import HomeView

def home(request):
    home = HomeView()
    langs = home.get_langs()
    bio = home.bio()
    social = home.socal_links()
    expertise = home.expertise()
    skills = home.skills()

    data = {
        'langs': langs,
        'bio': bio,
        'social': social,
        'expertise': expertise,
        'skills': skills,
    }

    return(
        render(request, 'index.html', data)
    )
