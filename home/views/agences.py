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
        form = AgencesForm(request.POST, request.FILES)
        if form.is_valid():
            agence = form.save(commit=False)
            agence.creator = request.user
            agence.save()
            messages.success(request, _('Agence created Successfully. Please check your mail box and hit the mail verification.'))
            return redirect(reverse('index'))
        else:
            return render(request, 'agences/register.html', {'form_reg': form, 'action_name': _('Register')}, status=200)


class ManageAgenceView(AgencesView):
    template_name = "agences/manage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agence'] = self.request.user.agences_set.first()
        return context

    def post(self, request, *args, **kwargs):
        agence = self.request.user.agences_set.first()
        form = AgencesForm(request.POST, request.FILES, instance=agence)
        if form.is_valid():
            form.save()
            messages.success(request, _('Agence updated Successfully.'))
            return redirect(reverse('manage_agence'))
        else:
            return render(request, 'agences/manage.html', {'form': form, 'action_name': _('Manage')}, status=200)
