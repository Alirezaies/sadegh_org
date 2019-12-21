from django import forms
from ...models import ContactForm

class ContactUsForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder':'Your message here!'}
        ),
        max_length=4000,
        help_text='Maximum 4000 Characters.'
    )

    class Meta:
        model = ContactForm
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]