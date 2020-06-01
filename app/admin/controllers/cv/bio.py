from django.views.generic import UpdateView
from django.urls import reverse_lazy

from admin.controllers.views import SuperUserPermissionMixin
from admin.controllers.forms.edit_bio_form import EditBioForm
from alirezaies.models.bio_model import Bio

class BioView(SuperUserPermissionMixin, UpdateView):
    """
    update the bio in landing page
    """

    model = Bio
    context_object_name = 'bio_context'
    template_name = 'admin/cv/bio.html'
    form_class = EditBioForm
    success_url = reverse_lazy('cv_bio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit CV'

        return context

    def get_object(self):
        model_object = Bio.objects.all().order_by('-pk').first()

        return model_object
