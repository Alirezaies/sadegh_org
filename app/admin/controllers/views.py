from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

class SuperUserPermissionMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    validates the superuser permissions
    """
    def test_func(self):
        return self.request.user.is_superuser
