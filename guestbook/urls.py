from django.conf.urls import patterns, url

urlpatterns = patterns('guestbook.views',
        url(r'^$', 'index', name='guestbook'),
        )

