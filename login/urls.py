from django.conf.urls import patterns, url
from django.contrib.auth.views import login

urlpatterns = patterns('login.views',
        url(r'^$', login, {'template_name': 'login.html'}),
        url(r'^logout/$', 'user_logout', name='logout'),
        )
