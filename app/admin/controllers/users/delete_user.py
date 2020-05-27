from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


@method_decorator(login_required, name='dispatch')
class DeleteUser(DeleteView):
    """
    delete a user
    TODO:
    **** IMPORTANT: THIS FUNCTION SHOULD NEVER DELETE THE OLDEST SUPER USER ****
    """

    model = User
    template_name = 'admin/users/delete_user.html'
    success_url = reverse_lazy('users_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete A User'

        return context

    def get_queryset(self):
        query_set = super().get_queryset().filter(pk=self.kwargs['pk'])

        return query_set
