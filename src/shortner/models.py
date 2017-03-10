from django.db import models

# Create your models here.

from .utils import code_generator


class UrlApp (models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)# in database this creates whole new column.
    updated = models.DateTimeField(auto_now=True) #everytime model is saved time value is set
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created


    def save(self, *args, **kwargs):
        print ("something")
        self.shortcode = code_generator()
        super(UrlApp, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)