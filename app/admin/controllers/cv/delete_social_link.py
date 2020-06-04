from django.views.generic import DeleteView
from django.urls import reverse_lazy

from alirezaies.models.social_links_model import SocialLinks
from admin.controllers.views import SuperUserPermissionMixin

class DeleteSocialLinkView(SuperUserPermissionMixin, DeleteView):
    """
    Deletes a social media link from db
    """

    model = SocialLinks
    template_name = 'admin/cv/social_links_delete.html'
    success_url = reverse_lazy('cv_view_social_link')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete A Social Link'

        return context
