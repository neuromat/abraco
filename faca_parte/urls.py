from django.conf.urls import url

from faca_parte import views

urlpatterns = [
    url(r'^registration/$', views.registration, name='registration'),
]
