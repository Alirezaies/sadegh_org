from django.views.generic import ListView
from django.urls import reverse_lazy

from admin.controllers.views import SuperUserPermissionMixin
from admin.controllers.forms.edit_bio_form import EditBioForm
from alirezaies.models.social_links_model import SocialLinks

class SocialLinkView(SuperUserPermissionMixin, ListView):
    """
    view the social media links
    """
    context_object_name = 'links'
    model = SocialLinks
    template_name = 'admin/cv/social_links_view.html'
    form_class = EditBioForm
    success_url = reverse_lazy('cv_view_social_link')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'View Social Links - CV'

        return context
