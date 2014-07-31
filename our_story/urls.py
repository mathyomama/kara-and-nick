from django.conf.urls import patterns, url

urlpatterns = patterns('our_story.views',
        url(r'^$', 'index', name='our_story'),
        )

