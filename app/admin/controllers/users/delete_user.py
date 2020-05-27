from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied


@user_passes_test(lambda user: user.is_superuser)
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
        forbidden_user_to_delete = User.objects.all().order_by('date_joined').first().username

        query_user = query_set[0].username

        if forbidden_user_to_delete == query_user:
            raise PermissionDenied

        return query_set
