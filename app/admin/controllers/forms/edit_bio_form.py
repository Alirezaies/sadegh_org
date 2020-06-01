import datetime
from django import forms

from alirezaies.models import Bio

years = []
now = datetime.datetime.now()

# init the years
for i in range(1980, now.year):
    years.append(str(i))

class EditBioForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.SelectDateWidget(years=years))

    class Meta:
        model = Bio
        fields = [
            'name',
            'role',
            'dob',
            'nationality',
            'image_url',
            'bio',
        ]
