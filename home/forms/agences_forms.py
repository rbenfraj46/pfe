from django import forms
from django.forms.fields import CharField
from django.forms.fields import EmailField
from django.forms.fields import BooleanField
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from home.models import Agences

User = get_user_model()


class AgencesForm(forms.Form):
    accept_term = BooleanField(required=True, label=_('Accept Terms'))

    class Meta:
        model = Agences
        fields = "__all__"
        exclude = ["creator", "creation_date", "update_date", "is_mail_verified", "is_active"]

    def __init__(self, *args, **kwargs):
        super(AgencesForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': _('The field ') + field.label + _(' is required')}

    def save(self, commit=True):
        agences = super().save(commit)
        agences.creator = self.request.user
        agences.is_mail_verified = False
        agences.is_active = False
        if commit:
            agences.save()
        return  agences

