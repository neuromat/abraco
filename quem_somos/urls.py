from django.conf.urls import url

from quem_somos import views


urlpatterns = [
    url(r'^$', views.who_we_are, name='who_we_are'),
]
