from django.conf.urls import patterns, url

urlpatterns = patterns('login.views',
        url(r'^$', 'index', name='login'),
        )

