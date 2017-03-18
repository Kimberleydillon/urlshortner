from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.

#functional view
def urlapp_redirect_view(request, *args, **kwargs):
    return HttpResponse("hello")

#class based view
class UrlCBView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello again")

