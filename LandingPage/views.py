from django.shortcuts import render

from django.views.generic.base import TemplateView

from LandingPage.models import Pagina, Empresa


class LandingPage(TemplateView):

    template_name = 'landing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pagina = Pagina.objects.filter(tipo='LANDING_PAGE').last()
        context['pagina'] = pagina
        context['empresa'] = Empresa.objects.last()
        return context