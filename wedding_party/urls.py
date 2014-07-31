from django.conf.urls import patterns, url

urlpatterns = patterns('wedding_party.views',
        url(r'^$', 'index', name='wedding_party'),
        )

