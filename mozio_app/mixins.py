from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from rnd_itr_app import models


class MessageMixin(object):

    @property
    def success_message(self):
        return ''

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, self.success_message)
        return super(MessageMixin, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, self.error_message)
        return super(MessageMixin, self).form_invalid(form)


class TemplateValuesMixin(object):

    @property
    def template_valuespage(self):
        return {}

    def get_context_data(self, **kwargs):
        context = super(TemplateValuesMixin, self).get_context_data(**kwargs)
        for each in self.template_values.keys():
            context[each] = self.template_values[each]
        return context


class ExtraDatasetMixin(object):

    @property
    def extra_dataset(self):
        return None

    def __init__(self):
        self._extra_dataset = {
            'frequency': {
                'data': models.Frequency.objects.all(),
                'link': str(reverse_lazy('frequency-create'))
            },
            'technology': {
                'data': models.Technology.objects.all(),
                'link': str(reverse_lazy('technology-create'))
            },
            'user': {
                'data': User.objects.filter(is_superuser=False),
                'link': str(reverse_lazy('user-create'))
            }
        }

    def get_extra_dataset(self, extra_dataset=None):
        """
        if extra_dataset is set:
            Return a dict with datasets including only models in extra_dataset
        if extra_dataset is not set:
            Return all datasets defined in __init__
        """
        # Parameter override class property
        if extra_dataset:
            self.extra_dataset = extra_dataset
        if self.extra_dataset:
            filtered = {}
            for each in self.extra_dataset:
                filtered[each] = self._extra_dataset[each]
            return filtered
        else:
            return self._extra_dataset

    def get_context_data(self, **kwargs):
        context = super(ExtraDatasetMixin, self).get_context_data(**kwargs)
        context['dataset'] = self.get_extra_dataset()
        return context
