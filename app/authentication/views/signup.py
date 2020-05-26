from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from .forms.signup_form import SignUpForm


def signup(request):
    err_flag = False

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            auth_login(request, user)
            return(
                redirect('home')
            )
            
        else:
            form = SignUpForm(request.POST)

            for field in form:
                if field.errors:
                    err_flag = True

            return render(
                request,
                'auth/auth.html',
                {
                    'title':'SignUp',
                    'form':form,
                    'err_flag': err_flag,
                }
            )
    
    form = SignUpForm()

    return render(
        request,
        'auth/auth.html',
        {
            'title':'SignUp',
            'form':form,
            'err_flag': err_flag,
        }
    )