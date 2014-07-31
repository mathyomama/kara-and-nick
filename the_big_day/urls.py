from django.conf.urls import patterns, url

urlpatterns = patterns('the_big_day.views',
        url(r'^$', 'index', name='the_big_day'),
        )

