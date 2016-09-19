from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addmovie$', views.addmovie),
    url(r'^addactor$', views.addactor),
	url(r'^movies/(?P<id>\d+)$', views.movie),
    url(r'^actors/(?P<id>\d+)$', views.actor)
]
