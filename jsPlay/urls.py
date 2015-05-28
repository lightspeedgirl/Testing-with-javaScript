from django.conf.urls import patterns, url
from jsPlay import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^test2$', views.test2, name ='test2'),
    url(r'^can$', views.can, name ='can'),
    url(r'^followMouse$', views.followMouse, name ='followMouse'),
    url(r'^lines$', views.lines, name ='lines'),
    url(r'^nirvash$', views.nirvash, name ='nirvash'),
    url(r'^rombasimiltion$', views.rombasimiltion, name ='rombasimiltion'),
)

