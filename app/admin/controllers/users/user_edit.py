from django.views.generic import UpdateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.urls import reverse_lazy

@user_passes_test(lambda user: user.is_superuser)
class EditUser(UpdateView):
    """
    edit a user
    **** IMPORTANT: THIS FUNCTION SHOULD NEVER DELETE THE OLDEST SUPER USER ****
    """
    model = User
    template_name = 'admin/users/edit_user.html'
    success_url = reverse_lazy('users_list')
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'is_superuser',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit User'

        return context
