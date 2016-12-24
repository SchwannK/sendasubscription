from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class ContactForm(forms.Form):
    contact_name = forms.CharField()
    contact_email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    helper = FormHelper()
    helper.layout = Layout(
        Field('contact_name', css_class='form-control-lg', wrapper_class='row'),
        Field('contact_email', css_class='form-control-lg', wrapper_class='row'),
        Field('content', rows="3", css_class='form-control-lg', wrapper_class='row'),
        Div(
            Div(
                Submit('Submit', 'Submit', css_class="btn-primary"),
                css_class='offset-sm-3 col-sm-9'
            ),
            css_class='form-group row'
        )
    )
    helper.label_class = 'col-sm-3'
    helper.field_class = 'col-sm-9'
