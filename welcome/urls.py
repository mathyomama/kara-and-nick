from django.conf.urls import patterns, url

urlpatterns = patterns('welcome.views',
        url(r'^$', 'index', name='welcome'),
        )

