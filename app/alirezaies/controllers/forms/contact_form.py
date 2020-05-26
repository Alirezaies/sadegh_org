from django import forms
from ...models import ContactForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class ContactUsForm(forms.ModelForm):
    #TODO: return captcha to the form for production :)
    # captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)

    class Meta:
        model = ContactForm
        fields = [
            'name',
            'email',
            'subject',
            'message',
            # 'captcha',
        ]