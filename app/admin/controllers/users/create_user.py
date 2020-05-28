from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from admin.controllers.views import SuperUserPermissionMixin

class CreateUserView(SuperUserPermissionMixin, CreateView):

    template_name = 'admin/users/create_user.html'
    form_class = UserCreationForm
    context_object_name = 'context'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create A New User'

        return context
