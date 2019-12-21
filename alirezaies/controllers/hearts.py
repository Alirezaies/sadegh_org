from django.shortcuts import render

def hearts_controller(request):
    return(
        render(request, 'hearts.html', {})
    )