from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from admin.controllers.views import SuperUserPermissionMixin


class UserProfileView(SuperUserPermissionMixin, ListView):
    """
    returns the user model, just for view :)
    nothing special (at all :D )
    """

    model = User
    template_name = 'admin/users/view_user.html'
    context_object_name = 'user_object'

    def get_queryset(self):
        query_set = get_object_or_404(User, username=self.kwargs['username'])

        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'View Profile'

        return context
