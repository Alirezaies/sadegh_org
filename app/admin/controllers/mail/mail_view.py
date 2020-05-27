from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from alirezaies.models.contact_form_model import ContactForm


@method_decorator(login_required, name='dispatch')
class MailView(ListView):
    """
    view a mail
    """

    context_object_name = 'mail'
    template_name = 'admin/mail/mail.html'

    def get_queryset(self):
        query_set = get_object_or_404(ContactForm, pk=self.kwargs['pk'])

        return query_set
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_queryset().subject

        return context