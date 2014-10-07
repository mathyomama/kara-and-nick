from django.conf.urls import patterns, url
from .views import InitialView, PersonCreate, PersonUpdate, PersonDelete

urlpatterns = patterns('rsvp.views',
        url(r'^$', InitialView.as_view(), name='rsvp-initial'),
        url(r'^create/$', PersonCreate.as_view(), name='rsvp-create'),
        url(r'^(?P<first_name>\w+)_(?P<last_name>\w+)/(?P<pk>[0-9]+)/update$', PersonUpdate.as_view(), name='rsvp-update'),
        url(r'^(?P<first_name>\w+)_(?P<last_name>\w+)/(?P<pk>[0-9]+)/delete$', PersonDelete.as_view(), name='rsvp-delete'),
        )

