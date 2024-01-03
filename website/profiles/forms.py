import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    HTML,
    Column,
    Div,
    Field,
    Layout,
    Row,
    Submit,
)
from django import forms
from django.utils.translation import gettext_lazy as _

from profiles import models

class ProfileCreationForm(forms.ModelForm):

    is_women = forms.BooleanField(
        label=_("La participante se considère comme une femme."),
        error_messages={
            "required": _(
                "Vous ne pouvez pas vous inscrire aux stages Girls Can Code! si vous ne vous considèrez pas comme femme."
            ),
        },
    )

    legal_authorization = forms.BooleanField(
        label=_(
            "La participante a plus de 15 ans OU l'autorisation de son responsable légal pour candidater à ce stage."
        ),
        error_messages={
            "required": _(
                "La participante ne peux pas s'inscrire à ce stage sans l'autorisation de son responsable légal ou si elle a 15 ans ou moins."
            ),
        },
    )

    class Meta:
        model = models.Profile
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "phone",
            "street_app",
            "complement_app",
            "city_app",
            "zipcode_app",
            "country_app",
            # Legal Guardian
            "first_name_resp",
            "last_name_resp",
            "email_resp",
            "phone_resp",
            "street_resp",
            "complement_resp",
            "city_resp",
            "zipcode_resp",
            "country_resp",
            # School
            "school_name",
            "street_school",
            "complement_school",
            "city_school",
            "zipcode_school",
            "country_school",
        )

    def __init__(self, *args, user, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.user = user
        self.helper = FormHelper()

        self.fields['birth_date'].widget.input_type = 'date'

        address_field_generator = lambda suffix: (
            Field(f'street_{suffix}'),
            Field(f'complement_{suffix}'),
            Row(
                Column(Field(f'city_{suffix}')),
                Column(Field(f'zipcode_{suffix}')),
                Column(Field(f'country_{suffix}')),
            )
        )

        self.helper.layout = Layout(
            Div(
                Div(
                    HTML("<h2>{}</h2>".format(_("Informations de la participante"))),
                    Row(
                        Column(Field("first_name")),
                        Column(Field("last_name")),
                    ),
                    Field("birth_date"),
                    Field("email"),
                    Field("phone"),
                    *address_field_generator('app'),
                    Field("is_women"),
                    Field("legal_authorization"),
                    css_class="col-sm-12 col-lg-6"
                ),
                Div(
                    HTML("<h2>{}</h2>".format(_("Informations sur l'établissement scolaire"))),
                    Field("school_name"),
                    *address_field_generator('school'),
                    css_class="col-sm-12 col-lg-6",
                ),
                Div(
                    HTML("<h2>{}</h2>".format(_("Informations du responsable légal"))),
                    Row(
                        Column(Field("first_name_resp")),
                        Column(Field("last_name_resp")),
                    ),
                    Field("email_resp"),
                    Field("phone_resp"),
                    *address_field_generator('resp'),
                    css_class="col-sm-12"
                ),
                Submit(
                    name="submit-application",
                    value="Créer mon profil",
                    css_class="my-4 btn btn-primary btn-block",
                ),
            css_class="row",
            )
        )
