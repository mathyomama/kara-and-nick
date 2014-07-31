from django.conf.urls import patterns, url

urlpatterns = patterns('things_to_do.views',
        url(r'^$', 'index', name='things_to_do'),
        )
