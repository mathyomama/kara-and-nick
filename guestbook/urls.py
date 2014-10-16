from django.conf.urls import patterns, url
from .views import GuestbookEntryCreate, GuestbookEntryUpdate, GuestbookEntryEditList, GuestbookEntryDelete, GuestbookEntryList, GuestbookEntryDetail

urlpatterns = patterns('guestbook.views',
        url(r'^$', GuestbookEntryList.as_view(), name='guestbook-list'),
        url(r'^page/(?P<page>\d+)/$', GuestbookEntryList.as_view(), name='guestbook-list-page'),
        url(r'^list/$', GuestbookEntryList.as_view()),
        url(r'^entry/(?P<pk>\d+)/$', GuestbookEntryDetail.as_view(), name='guestbook-detail'),
        url(r'^create/$', GuestbookEntryCreate.as_view(), name='guestbook-create'),
        url(r'^(?P<created_by>\w+)/edit/$', GuestbookEntryEditList.as_view(), name='guestbook-edit-list'),
        url(r'^(?P<created_by>\w+)/(?P<pk>\d+)/update/$', GuestbookEntryUpdate.as_view(), name='guestbook-update'),
        url(r'^(?P<created_by>\w+)/(?P<pk>\d+)/delete/$', GuestbookEntryDelete.as_view(), name='guestbook-delete'),
        )
