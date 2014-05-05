from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse
from mozio_app import forms
from mozio_app import models


@require_http_methods(['GET'])
def list(request):
    """ View for all the existing Providers in the database
    """
    template_values = {
        'page': {
            'title': 'Provider List'
        }
    }
    provider_list = models.Provider.objects.all()
    template_values['provider_list'] = provider_list
    return render(request, 'mozio_app/provider_list.html', template_values)


@require_http_methods(['GET', 'POST'])
def save(request, pk=None):
    """ View to save or update the information provided.
    """
    template_values = {
        'page': {
            'title': 'Provider List'
        }
    }
    if request.method == 'GET':
        if pk:
            provider = get_object_or_404(models.Provider, pk=pk)
            template_values['pk'] = provider.pk
            form = forms.Provider(instance=provider)
        else:
            form = forms.Provider()
        template_values['form'] = form
    elif request.method == 'POST':
        try:
            # Update the existing object
            provider = \
                models.Provider.objects.get(pk=request.POST.get('pk'))
            form = forms.Provider(request.POST, instance=provider)
            message = "Provider '{}' has been updated successfully".format(
                request.POST.get('name'))
        except models.Provider.DoesNotExist:
            # Create the Object
            form = forms.Provider(request.POST)
            message = "Provider '{}' has been inserted successfully".format(
                request.POST.get('name'))

        if form.is_valid():
            provider = form.save()
            messages.add_message(request, messages.SUCCESS, message)
            return redirect(reverse('provider-list'))
        else:
            template_values['form'] = form
    return render(request, 'mozio_app/provider_form.html', template_values)


@require_http_methods(['GET'])
def delete(request, pk):
    """ View to delete the requested Provider
    """
    provider = models.Provider.objects.get(pk=pk)
    provider.delete()
    return redirect(reverse('provider-list'))
