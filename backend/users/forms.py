from django import forms
from django.core.validators import validate_email
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, Row, Column, HTML

class PersonalInfoForm(forms.Form):
    first_name = forms.CharField(
        label = "Prénom",
        max_length = 80,
        required = True
    )

    last_name = forms.CharField(
        label = "Nom",
        max_length = 80,
        required = True,
    )

    street = forms.CharField(
        label = "Nom et numéro de voie",
        max_length = 256,
        required = False,
    )

    zip_code = forms.CharField(
        label = "Code postal",
        max_length = 10,
        required = False,
    )

    city = forms.CharField(
        label = "Ville",
        max_length = 80,
        required = False,
    )

    country = forms.CharField(
        label = "Pays",
        max_length = 80,
        required = False,
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'personal_info_form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        name_layout = Row(
                Column(Field('last_name', placeholder = self.fields['last_name'].label)),
                Column(Field('first_name', placeholder = self.fields['first_name'].label)),
                )
        address_layout = Div(
            HTML("<div style=\"margin-bottom: 8px\">Adresse</div>"),
            Row(Field('street', placeholder = self.fields['street'].label,)),
            Row(
                Column(Field('zip_code', placeholder = self.fields['zip_code'].label)),
                Column(Field('city',placeholder = self.fields['city'].label)),
                ),
            Row(Field('country', placeholder = self.fields['country'].label)),
        )

        # Disable the label of address fields
        self.fields['street'].label = False
        self.fields['zip_code'].label = False
        self.fields['city'].label = False
        self.fields['country'].label = False

        self.helper.layout = Layout(
            name_layout,
            address_layout,
            Submit('submit', 'Sauvegarder', css_class='btn btn-primary'),
        )

class EmailForm(forms.Form):
    email = forms.EmailField(
            label="E-mail",
            max_length=320,
            required=True,
            validators=[validate_email]
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'personal_info_form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.layout = Layout(
            Field('email', placeholder = "Nouvelle adresse e-mail"),
            Submit('submit', 'Sauvegarder')
        )