from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    HTML,
    Button,
    Column,
    Div,
    Field,
    Layout,
    Row,
    Submit,
)
from django import forms
from django.utils.translation import gettext_lazy as _

class EventSignupForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "application_form"
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            Div(
                Field("first_name"),
                Field("last_name"),
                Div(
                    Button(
                        name="next",
                        value="Suivant",
                        css_class="btn primary-button",
                    ),
                    css_class="mt-4 p-0",
                ),
            ),
        )
