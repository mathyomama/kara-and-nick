from django.conf.urls import patterns, url

urlpatterns = patterns('contacts.views',
        url(r'^$', 'index', name='contacts'),
        )
