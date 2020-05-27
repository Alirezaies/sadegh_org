from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@method_decorator(login_required, name='dispatch')
class UsersList(ListView):
    """
    users list view
    """
    model = User
    template_name = 'admin/users/users.html'
    context_object_name = 'users_list'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Users List'

        return context
    
    def get_queryset(self):
        query_set = super().get_queryset().order_by('-date_joined')

        return query_set