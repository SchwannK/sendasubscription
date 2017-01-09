from django import forms
from django.core.validators import RegexValidator

class GiftForm(forms.Form):

    giftee_postcode = forms.RegexField(label='Postcode', min_length=5, required=True, max_length=100, regex=r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}', error_message="Please enter a valid UK postcode")
    giftee_first_name = forms.CharField(label='First name', max_length=50)
    giftee_last_name = forms.CharField(label='Last name', max_length=50)
    giftee_email = forms.EmailField(label='Email', max_length=200)

    giftee_address_line1 = forms.CharField(label='Address Line 1', max_length=100)
    giftee_address_line2 = forms.CharField(label='Address Line 2', max_length=100, required=False)
    giftee_city = forms.CharField(label='City', max_length=100)

    giftee_country = forms.CharField(label='Country', max_length=100, initial='United Kingdom', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
