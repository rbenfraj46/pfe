from django import forms
from django.utils.translation import gettext_lazy as _

from home.models import Devise


class DeviseForm(forms.Form):

    devise = forms.CharField(max_length=255, required=True, label=_('Devise'),
                             widget=forms.Select(
                                 choices=Devise.objects.filter(is_active=True).all()))
    next = forms.CharField(max_length=4096, required=True, label=_('Next'))
