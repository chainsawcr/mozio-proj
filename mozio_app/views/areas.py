from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse
from mozio_app import forms
from mozio_app import models


@require_http_methods(['GET'])
def list(request):
    """ View for all the Areas
    """
    template_values = {
        'page': {
            'title': 'Areas'
        }
    }
    area_list = models.Area.objects.all()
    template_values['area_list'] = area_list
    return render(request, 'mozio_app/area_list.html', template_values)


@require_http_methods(['GET', 'POST'])
#@login_required
def save(request, pk=None):
    """ View to save or update the information provided.
    """
    template_values = {
        'page': {
            'title': 'Area'
        }
    }
    if request.method == 'GET':
        if pk:
            area = get_object_or_404(models.Area, pk=pk)
            template_values['pk'] = area.pk
            form = forms.Area(instance=area)
        else:
            form = forms.Area()
        template_values['form'] = form
    elif request.method == 'POST':
        try:
            # Update the existing object
            area = \
                models.Area.objects.get(pk=request.POST.get('pk'))
            form = forms.Area(request.POST, instance=area)
            message = "Map Area '{}' has been updated successfully".format(
                request.POST.get('name'))
        except models.Area.DoesNotExist:
            # Create the Object
            form = forms.Area(request.POST)
            message = "Map Area '{}' has been inserted successfully".format(
                request.POST.get('name'))

        if form.is_valid():
            area = form.save()
            messages.add_message(request, messages.SUCCESS, message)
            return redirect(reverse('map-list'))
        else:
            template_values['form'] = form
    return render(request, 'mozio_app/area_form.html', template_values)


@require_http_methods(['GET'])
def delete(request, pk):
    """ View to delete the requested Provider
    """
    area = models.Provider.objects.get(pk=pk)
    area.delete()
    return redirect(reverse('map-list'))
