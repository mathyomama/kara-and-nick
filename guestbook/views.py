from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from .models import GuestbookEntry

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import GuestbookEntryForm
from django.utils.decorators import method_decorator
from rsvp.models import Person

class GuestbookMixin(object):

    def get_context_data(self, *args, **kwargs):
        kw_args = super(GuestbookMixin, self).get_context_data(*args, **kwargs)
        kw_args['side_menu'] = "Welcome to the guestbook. Please feel free to write a message for the couple or view other's notes. To add a message click \"Create Post\" and fill out the form. You may change or delete your post, as well, by clicking \"Edit Post.\""
        return kw_args

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GuestbookMixin, self).dispatch(*args, **kwargs)

class GuestbookEntryList(GuestbookMixin, ListView):
    """
    This is the first view the user will look at when navigating to the guestbook. It will have all the
    guestbook entries paginate and truncated.
    """
    model = GuestbookEntry
    context_object_name = 'guestbook_entries'
    template_name = 'guestbook/list.html'
    paginate_by = 10

class GuestbookEntryDetail(GuestbookMixin, DetailView):
    """
    This is the detail view which further expounds on the guestbook entry seen in the list view.
    """
    model = GuestbookEntry
    context_object_name = 'entry'
    template_name = 'guestbook/entry.html'

class AjaxableResponseMixin(object):
    """
    This is for handling AJAX requests and sending out the proper information on success or fail. This will
    be used by the create, update, and delete views.
    """
    status = None

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        old_id = None
        if self.status == 'update':
            old_id = GuestbookEntry.objects.get(pk=self.kwargs[self.pk_url_kwarg]).get_html_id()
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            post = self.object
            data = {
                    'name': post.name,
                    'location': post.location,
                    'note': post.note,
                    'id': post.get_html_id(),
                    'absolute_url': post.get_absolute_url(),
                    'update_url': post.get_absolute_update_url(),
                    'delete_url': post.get_absolute_delete_url(),
                    'status': self.status,
                    'old_id': old_id,
                    }
            return JsonResponse(data)
        else:
            return response
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        old_id = self.object.get_html_id()
        success_url = self.get_success_url()
        self.object.delete()
        if request.is_ajax():
            data = {
                    'status': self.status,
                    'old_id': old_id,
                    }
            return JsonResponse(data)
        else:
            return HttpResponseRedirect(success_url)

class GuestbookEntryFormMixin(object):
    """
    This helps with grabbing the right information for the form. Since the create and update forms are very
    similar, they will be using a lot of the same information. For each form view, the account of the person
    need to be pulled up in order to check the number of reservations and other queries. This information
    may change from request to request, which could be AJAX, so the account needs to be re-queried from the
    database.
    """
    form_class = GuestbookEntryForm
    model = GuestbookEntry
    fields = [
            'name',
            'location',
            'note',
            ]
    template_name = 'guestbook/guestbook_form.html'
    modal_template_name = 'guestbook/guestbook_form_modal.html'
    status = None
    status_button = "submit"
    form_title = "Guestbook Entry Form"
    not_allowed_message = "You can't fill out anymore guestbook entries, sorry."
    success_url = reverse_lazy('guestbook-list')
    notes_limit = 15

    def get_context_data(self, *args, **kwargs):
        kw_args = super(GuestbookEntryFormMixin, self).get_context_data(*args, **kwargs)
        kw_args['not_allowed_message'] = _(self.not_allowed_message)
        kw_args['status'] = _(self.status)
        kw_args['status_button'] = _(self.status_button)
        kw_args['form_title'] = _(self.form_title)
        return kw_args

    def get_template_names(self):
        template_name = super(GuestbookEntryFormMixin, self).get_template_names()
        if self.request.is_ajax():
            return [self.modal_template_name]
        else:
            return template_name

class GuestbookEntryCreate(AjaxableResponseMixin, GuestbookEntryFormMixin, GuestbookMixin, CreateView):
    """
    This is for creating a guestbook entry with or without Ajax.
    """
    form_class = GuestbookEntryForm
    context_object_name = 'form'
    template_name = 'guestbook/guestbook_form.html'
    status = 'create'
    form_title = 'Add a Note'

    def get(self, request):
        account_notes_count = GuestbookEntry.objects.filter(created_by=request.user).count()
        if account_notes_count < self.notes_limit:
            return super(GuestbookEntryCreate, self).get(request)
        else:
            form = None
            context_dict = self.get_context_data(form=form)
            return self.render_to_response(context_dict)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(GuestbookEntryCreate, self).form_valid(form)

class GuestbookEntryEditList(GuestbookMixin, ListView):
    """
    This will list the guestbook entries which the user can modify
    """
    context_object_name = 'user_entries'
    template_name = 'guestbook/edit_list.html'

    def get_queryset(self):
        return GuestbookEntry.objects.filter(created_by=self.request.user)
 
class ModifyMixin(object):
    """
    This is for any view which will modify the database, so the update and delete views. It adds a check for
    the user so that user can't modify other's information.
    """

    def get(self, request, *args, **kwargs):
        response = super(ModifyMixin, self).get(request, *args, **kwargs)
        return response
        if self.object.created_by == request.user:
            return response
        else:
            return not_allowed(request)

class GuestbookEntryUpdate(ModifyMixin, AjaxableResponseMixin, GuestbookEntryFormMixin, GuestbookMixin, UpdateView):
    """
    This is the for updating the guestbook entry.
    """
    form_class = GuestbookEntryForm
    model = GuestbookEntry
    context_object_name = 'form'
    template_name = 'guestbook/guestbook_form.html'
    status = 'update'
    form_title = 'Edit Note'

class GuestbookEntryDelete(ModifyMixin, AjaxableResponseMixin, GuestbookEntryFormMixin, GuestbookMixin, DeleteView):
    """
    This is for deleting the guestbook entry.
    """
    model = GuestbookEntry
    context_object_name = 'entry'
    success_url = reverse_lazy('guestbook-list')
    template_name = 'guestbook/delete_form.html'
    modal_template_name = 'guestbook/delete_form_modal.html'
    form_message = "Are you sure you want to delete this note. You could just change it."
    status = 'delete'
    form_title = 'Delete Note'

    def get_context_data(self, *args, **kwargs):
        kw_args = super(GuestbookEntryDelete, self).get_context_data(*args, **kwargs)
        kw_args['form_message'] = _(self.form_message)
        kw_args['form_title'] = _(self.form_title)
        return kw_args

def not_allowed(request):
    """
    The method for 'not allowed' message. Use this to show the user he or she is not allowed to do whatever
    action he or she was about to perform. This will redirect to a page with the following message.
    """
    data = {
            "status": "not_allowed",
            "form_message": "You are not allowed to edit or delete this reservation.",
            }
    if request.is_ajax():
        return JsonResponse(data)
    else:
        return render(request, "rsvp/not_allowed.html", data)
