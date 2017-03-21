from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.

#functional view
def urlapp_redirect_view(request, shortcode=None, *args, **kwargs):
    return HttpResponse("hello {sc}".format(sc=shortcode))

#class based view
class UrlCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse("hello again {sc}".format(sc=shortcode))

