from django.views.generic import ListView

from alirezaies.models.contact_form_model import ContactForm
from admin.controllers.views import SuperUserPermissionMixin

class MailBoxView(SuperUserPermissionMixin, ListView):
    """
    List all the mails in the mailbox
    """

    model = ContactForm
    context_object_name = 'mailbox_context'
    template_name = 'admin/mail/mailbox.html'
    paginate_by = 20

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
