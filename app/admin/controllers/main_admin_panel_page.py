from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from alirezaies.models.contact_form_model import ContactForm

@user_passes_test(lambda user: user.is_superuser)
def main_admin_panel_func(request):
    """
    this function handles the index page of the admin panel
    """

    # get user's last login
    username = request.user.username
    last_login = User.objects.get(username=username).last_login

    messages_count = ContactForm.objects.all().count()

    # in case we have no messages
    if messages_count == 0:
        messages_info = None
    else:
        messages_info = {}
        latest_message = ContactForm.objects.all().last()

        messages_info.update(latest_message=latest_message)
        messages_info.update(messages_count=messages_count)

    # get last 3 users
    last_three_users = User.objects.all().order_by('-id')[:3]

    # return data
    return render(
        request,
        'admin/index.html',
        {
            'title': 'Admin Dashboard',
            'last_login': last_login,
            'messages_info': messages_info,
            'last_three_users': last_three_users,
        }
    )
