from django.core.urlresolvers import reverse
from django.db import models
import os
import uuid

# Create your models here.


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('files', filename)


class Provider(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('technology-list')
        return reverse('provider-update', kwargs={'pk': self.pk})


class Area(models.Model):
    name = models.CharField(max_length=50, unique=True)
    #provider = models.ForeignKey('Provider', null=False)
    points = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('area-update', kwargs={'pk': self.pk})
