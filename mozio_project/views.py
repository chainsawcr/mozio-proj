from django.views.generic.base import TemplateView, RedirectView


class HomeTemplateView(TemplateView):
    template_name = "base.html"
