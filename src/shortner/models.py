from django.conf import settings
from django.db import models

# Create your models here.

from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class UrlAppManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(UrlAppManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = UrlApp.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items] #reverses query set by reverse order of ids
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class UrlApp (models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)# in database this creates whole new column.
    updated = models.DateTimeField(auto_now=True) #everytime model is saved time value is set
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created
    active = models.BooleanField(default=True)
    objects = UrlAppManager()
    some_random = UrlAppManager()

    def save(self, *args, **kwargs): #overrides save method
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(UrlApp, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)