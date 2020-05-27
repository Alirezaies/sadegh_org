from django.views.generic import DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy

from alirezaies.models.contact_form_model import ContactForm

@user_passes_test(lambda user: user.is_superuser)
class DeleteMail(DeleteView):
    """
    delete a mail
    """
    
    model = ContactForm
    template_name = 'admin/mail/delete_mail.html'
    success_url = reverse_lazy('mailbox')

    def get_queryset(self):
        query_set = super().get_queryset().filter(pk=self.kwargs['pk'])

        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete: ' + self.get_queryset()[0].subject

        return context
