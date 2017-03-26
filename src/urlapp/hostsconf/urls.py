from django.conf.urls import url

from .views import wildcard_redirect

urlpatterns = [
    url(r'^( ?P <path>.*)', admin.site.urls),
]
