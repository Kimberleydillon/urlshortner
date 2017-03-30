from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import UrlApp


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context= {
            "title": "Snazzy Url",
            "summary": "Shorten your urls and enjoy more room on your sweet tweets for your thoughts!",
            "form": the_form
        }
        return render(request,"shortener/home.html", context)

    def post (self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        context = {
            "title": "Snazzy Url",
            "summary": "Add your new Snazztacular url is ",
            "form": form
        }
        return render(request, "shortener/home.html", context)


#class based view.url
class UrlCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs): #In class based view you have to explicitly write out the method.
        obj = get_object_or_404(UrlApp, shortcode=shortcode)
        shortcode = obj.shortcode
        return HttpResponse("hello again {sc}".format(sc=obj.url)) #take more code to write but are more portable

    def post ( self, request, *args, **kwargs):
        return HttpResponse()