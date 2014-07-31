from django.conf.urls import patterns, url

urlpatterns = patterns('rsvp.views',
        url(r'^$', 'index', name='rsvp'),
        )

