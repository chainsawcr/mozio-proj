from django.views.generic.base import TemplateView


class Home(TemplateView):
    page = {
        'title': 'Dashboard',
        'subtitle': 'Statistics and more'
    }
    template_name = 'base.html'
