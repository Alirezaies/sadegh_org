from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
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
