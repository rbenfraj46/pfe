from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls.base import reverse
from django.utils.translation import gettext_lazy as _

from home.forms.agences_forms import AgencesForm


# Create your views here.
class AgencesView(LoginRequiredMixin, TemplateView):
    template_name =  "agences.html"


class RegisterView(AgencesView):
    template_name =  "agences/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = [{'Ariana':['Ariana','Sokra','Borj Louzir']},{'Ben Arous':['Ben Arous','Megrine','Rades']},{'Tunis':['Tunis','Bardo','Lac']}]
        return context

    def post(self, request, *args, **kwargs):
        form = AgencesForm(request.POST)
        if form.is_valid():
            messages.success(request, _('Agence created Successfully. Please check your mail box and hit the mail verification.'))
            return redirect(reverse('index'))
        else:
            return render(request, 'agences/register.html', {'form_reg': form, 'action_name': _('Register')}, status=200)
