from django.conf.urls import url

from faca_parte import views

urlpatterns = [
    url(r'^$', views.registration, name='registration'),
]
