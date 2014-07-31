from django.conf.urls import patterns, url

urlpatterns = patterns('registry.views',
        url(r'^$', 'index', name='registry'),
        )

