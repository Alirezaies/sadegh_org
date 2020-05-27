from django.views.generic import ListView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

@user_passes_test(lambda user: user.is_superuser)
class UserProfileView(ListView):
    """
    returns the user model, just for view :)
    nothing special (at all :D )
    """

    model = User
    template_name = 'admin/users/view_user.html'
    context_object_name = 'user_object'

    def get_queryset(self):

        # check if the user is authenticated to view this page
        if self.request.user.is_superuser:
            query_set = get_object_or_404(User, username=self.kwargs['username'])

        elif self.kwargs['username'] != self.request.user.username:
            raise PermissionDenied
        else:
            query_set = get_object_or_404(User, username=self.request.user.username)

        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'View Profile'

        return context
