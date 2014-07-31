from django.conf.urls import patterns, url

urlpatterns = patterns('gallery.views',
        url(r'^$', 'index', name='gallery'),
        )

