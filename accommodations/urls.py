from django.conf.urls import patterns, url

urlpatterns = patterns('accommodations.views',
        url(r'^$', 'index', name='accommodations'),
        )
