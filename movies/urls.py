from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.movie_list, name='movie_list'),
    url(r'^movie$', views.movie_list, name='movie_list'),
]