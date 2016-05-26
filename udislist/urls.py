"""udislist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse


def age(request, name, val):
    return HttpResponse("My name is {} and Im {} years old.".format(name.title(), val))


def mul(request, val_1, val_2):
    return HttpResponse("{} x {} = {}".format(val_1, val_2, eval(val_1 + '*' + val_2)))


def home(request):
    # assert False, "Boom!"
    # return HttpResponse("<b>Hello<b/> world", content_type="text/plain", status=404)
    return HttpResponse("<b>Hello<b/> world", status=404)


urlpatterns = [
    url(r'^x/(?P<val_1>\d+)/(?P<val_2>\d+)/$', mul),
    url(r'^age/(?P<name>[A-z]+)/$',age, kwargs={'val': '32'}),
    url(r'^age/(?P<val>\d+)/$',age, kwargs={'name': 'Avi'}),
    url(r'^age/(?P<name>\w+)/(?P<val>\d+)/$', age),
    url(r'^age/(?P<val>\d+)/(?P<name>\w+)/$', age),
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
]
