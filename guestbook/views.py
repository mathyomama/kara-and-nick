from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import GuestbookEntry

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import GuestbookEntryForm
from django.utils.decorators import method_decorator
from rsvp.models import Person

class GuestbookEntryCreate(CreateView):
    form_class = GuestbookEntryForm
    context_object_name = 'form'
    template_name = 'guestbook/create_form.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GuestbookEntryCreate, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self, *args, **kwargs):
        kw_args = super(GuestbookEntryCreate, self).get_form_kwargs(*args, **kwargs)
        kw_args['people'] = Person.objects.filter(account__user=self.request.user)
        return kw_args

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(GuestbookEntryCreate, self).form_valid(form)

#    def get_context_data(self, **kwargs):
#        context = super(GuestbookEntryCreate, self).get_context_data(**kwargs)
#        context['create

class GuestbookEntryUpdateList(ListView):
    context_object_name = 'user_entries'
    template_name = 'guestbook/update_list.html'

    def get_queryset(self):
        return GuestbookEntry.objects.filter(created_by=self.request.user)
 
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GuestbookEntryUpdateList, self).dispatch(*args, **kwargs)

class GuestbookEntryUpdate(UpdateView):
    form_class = GuestbookEntryForm
    context_object_name = 'form'
    template_name = 'guestbook/update_form.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GuestbookEntryUpdate, self).dispatch(*args, **kwargs)

class GuestbookEntryDeleteList(ListView):
    context_object_name = 'user_entries'
    template_name = 'guestbook/delete_list.html'

    def get_queryset(self):
        return GuestbookEntry.objects.filter(created_by=self.request.user)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GuestbookEntryDeleteList, self).dispatch(*args, **kwargs)

class GuestbookEntryDelete(DeleteView):
    model = GuestbookEntry
    success_url = reverse_lazy('guestbook-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GuestbookEntryDelete, self).dispatch(*args, **kwargs)

class GuestbookEntryList(ListView):
    model = GuestbookEntry
    context_object_name = 'guestbook_entries'
    template_name = 'guestbook/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GuestbookEntryList, self).dispatch(*args, **kwargs)

class GuestbookEntryDetail(DetailView):
    model = GuestbookEntry
    context_object_name = 'entry'
    template_name = 'guestbook/entry.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GuestbookEntryDetail, self).dispatch(*args, **kwargs)



@login_required
def index(request):
    clicks = 0
    if request.method == 'POST':
        pass
        '''
        if request['POST'] and request.POST['delete']:
            # verify that the person can delete it (unnecessary b/c of csrftoken)
            # find object from post id
            entry_num_on_page = request.POST['delete']
            entry_in_db = GuestbookEntry.objects.get(entry_num=entry_num_on_page)
            # delete fetched post
            entry_in_db.delete()
        '''

        if request.is_ajax():
            name = request.POST['name']
            city = request.POST['city']
            message = name + ' lives in ' + city
            return HttpResponse(json.dumps({'message': message})) 
            '''
            # create new post object
            new_entry = GuestbookEntry(name="Bugs Bunny", note="duck season", location="albequerque, nm")
            # save new entry object to database
            clicks += 1
            new_entry.save()
            '''

    context = RequestContext(request)
    context_dict = dict()

    # add guestbook entry form here, and put it in context dict

    posts = GuestbookEntry.objects.all()
    context_dict['posts'] = posts
    context_dict['clicks'] = str(clicks)

    return render_to_response("guestbook.html", context_dict, context)
