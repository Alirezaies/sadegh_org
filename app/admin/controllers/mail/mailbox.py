from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from alirezaies.models.contact_form_model import ContactForm

# TODO: login required
@method_decorator(login_required, name='dispatch')
class MailBoxView(ListView):
    """
    List all the mails in the mailbox
    """

    model = ContactForm
    context_object_name = 'mailbox_context'
    template_name = 'admin/mail/mailbox.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mailbox'

        return context
    
    def get_queryset(self):
        """
        query_set should be order in order to paginate :)
        """
        query_set = super().get_queryset().order_by('-date')

        return query_set
