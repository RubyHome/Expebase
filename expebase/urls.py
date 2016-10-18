from django.conf.urls import url

from . import views

app_name = "expebase"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard', views.dashboard , name='dashboard'),
    url(r'^result', views.result , name = "result"),
]