from django.shortcuts import render

def nil_controller(request):
    return(
        render(request, 'nil.html', {})
    )