from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wedding.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accommodations/', include('accommodations.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^guestbook/', include('guestbook.urls')),
    url(r'^our_story/', include('our_story.urls')),
    url(r'^registry/', include('registry.urls')),
    url(r'^rsvp/', include('rsvp.urls')),
    url(r'^the_big_day/', include('the_big_day.urls')),
    url(r'^wedding_party/', include('wedding_party.urls')),
    url(r'^things_to_do/', include('things_to_do.urls')),
    url(r'^welcome/', include('welcome.urls')),
    url(r'^$', include('login.urls')),
    url(r'^login/$', include('login.urls')),
)
