from django.conf.urls import patterns, url

urlpatterns = patterns('fonts.views',
        url(r'^$', 'index', name='fonts'),
        )

