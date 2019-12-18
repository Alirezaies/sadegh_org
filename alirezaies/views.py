from django.shortcuts import render
from .scripts.home import HomeView

def home(request):
    home = HomeView()
    langs = home.get_langs()
    bio = home.bio()
    social = home.socal_links()
    expertise = home.expertise()
    skills = home.skills()
    experience = home.experience()
    contact_info = home.contact_info()

    data = {
        'langs': langs,
        'bio': bio,
        'social': social,
        'expertise': expertise,
        'skills': skills,
        'exp': experience,
        'c_info': contact_info,
    }

    return(
        render(request, 'index.html', data)
    )

def hearts(request):
    return(
        render(request, 'hearts.html', {})
    )


def nil(request):
    return(
        render(request, 'nil.html', {})
    )