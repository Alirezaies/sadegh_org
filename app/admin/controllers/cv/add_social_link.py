from django.views.generic import CreateView
from django.urls import reverse_lazy

from admin.controllers.views import SuperUserPermissionMixin
from alirezaies.models.social_links_model import SocialLinks

class AddSocialLinkView(SuperUserPermissionMixin, CreateView):
    """
    create the social media links in landing page
    """

    model = SocialLinks
    template_name = 'admin/cv/social_links_add.html'
    success_url = reverse_lazy('cv_add_social_link')
    fields = [
        'name',
        'link',
        'icon_class',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Social Links - CV'

        return context
