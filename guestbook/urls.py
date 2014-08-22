from django.conf.urls import patterns, url
from .views import GuestbookEntryCreate, GuestbookEntryUpdate, GuestbookEntryDelete, GuestbookEntryList, GuestbookEntryDetail

urlpatterns = patterns('guestbook.views',
        #url(r'^$', 'index', name='guestbook'),
        url(r'^$', GuestbookEntryList.as_view(), name='guestbook-list'),
        url(r'^create/$', GuestbookEntryCreate.as_view(), name='guestbook-create'),
        url(r'^(?P<created_by>\w+)/(?P<pk>\d+)/update/$', GuestbookEntryUpdate.as_view(), name='guestbook-update'),
        url(r'^(?P<created_by>\w+)/(?P<pk>\d+)/delete/$', GuestbookEntryDelete.as_view(), name='guestbook-delete'),
        url(r'^(?P<created_by>\w+)/(?P<pk>\d+)/$', GuestbookEntryDetail.as_view(), name='guestbook-detail'),
        )

