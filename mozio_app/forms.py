from django import forms
from django.forms import ModelForm
from mozio_app import models


class Area(ModelForm):

    class Meta:
        model = models.Area
        fields = ('name', 'points')
        widgets = {
            'name': forms.widgets.TextInput(attrs={
                'class': 'm-wrap medium',
                'placeholder': "Area's descriptive name"
            }),
            'points': forms.widgets.TextInput(attrs={
                'class': 'm-wrap medium',
                'placeholder': "Area defined points"
            })
        }

    def __init__(self, *args, **kwargs):
        super(Area, self).__init__(*args, **kwargs)
        self.fields['provider'] = \
            forms.ModelChoiceField(
                queryset=models.Provider.objects.all(),
                empty_label=None
            )


class Provider(ModelForm):

    class Meta:
        model = models.Provider
        fields = ('name', 'description')
        widgets = {
            'name': forms.widgets.TextInput(attrs={
                'class': 'm-wrap medium',
                'placeholder': "Provider name"
            }),
            'description': forms.widgets.TextInput(attrs={
                'class': 'm-wrap medium',
                'placeholder': "Provider description"
            })
        }

