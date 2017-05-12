from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/id/
    url(r'^(?P<album_id>[0-9]+)$', views.detail, name='detail'),

    # /music/id/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),

    # register
    url(r'^register/$', views.UserFormView.as_view, name='register'),
 ]
