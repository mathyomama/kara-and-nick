from collections import OrderedDict
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import ugettext_lazy as _

from .forms import PersonForm
from .models import Account, Person, Image

class InitialView(TemplateView):
    """
    This is the first view the user will see when the go the rsvp page. Most of the content will be modified
    through AJAX, so the user will most likely be staying on this page.
    """
    template_name = 'rsvp/initial.html'
    instructions = "Please RSVP below. Click the &quotAdd Person&quot button to add a reservation. You may edit or delete a reservation, as well. In the reservation form please provide a <em>first name</em> and <em>last name</em>. You may optionally provide allergy infromation and your email for updates. This infromation won't be viewable by the public."

    def get(self, request):
        user_account = get_object_or_404(Account, user=request.user)
        people = Person.objects.filter(account=user_account)
        filled_spots = len(people)
        label = OrderedDict(
                [
                    ('first_name', _('First Name')),
                    ('last_name', _('Last Name')),
                    ('dietary_concerns', _('Dietary Concerns')),
                    ('email', _('Email')),
                    ('updates', _('Updates')),
                    ]
                )
        initial_dict = {
                'people': people,
                'reservations': user_account.reservations,
                'filled_spots': filled_spots,
                'label': label,
                'instructions': self.instructions,
                }
        context_dict = self.get_context_data(**initial_dict)

        return self.render_to_response(context_dict)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InitialView, self).dispatch(*args, **kwargs)

class AjaxableResponseMixin(object):
    """
    This is for handling AJAX requests and sending out the proper information on success or fail. This will
    be used by the create, update, and delete views.
    """

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        old_id = None
        if self.status == 'update':
            old_id = Person.objects.get(pk=self.kwargs[self.pk_url_kwarg]).get_html_id()
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            p = self.object
            data = {
                    'first-name': p.first_name,
                    'last-name': p.last_name,
                    'dietary-concerns': p.dietary_concerns,
                    'email': p.email,
                    'updates': p.updates,
                    'id': p.get_html_id(),
                    'update_url': p.get_absolute_update_url(),
                    'delete_url': p.get_absolute_delete_url(),
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

class PersonFormMixin(object):
    """
    This helps with grabbing the right information for the form. Since the create and update forms are very
    similar, they will be using a lot of the same information. For each form view, the account of the person
    need to be pulled up in order to check the number of reservations and other queries. This information
    may change from request to request, which could be AJAX, so the account needs to be re-queried from the
    database.
    """
    form_class = PersonForm
    model = Person
    fields = [
            'first_name',
            'last_name',
            'dietary_concerns',
            'email',
            'updates',
            ]
    template_name = 'rsvp/person_form.html'
    modal_template_name = 'rsvp/person_form_modal.html'
    status = None
    status_button = "button"
    form_title = "Reservation Form"
    not_allowed_message = "You don't have anymore reservations, sorry."
    post_url = None

    def get_context_data(self, *args, **kwargs):
        kw_args = super(PersonFormMixin, self).get_context_data(*args, **kwargs)
        kw_args['not_allowed_message'] = _(self.not_allowed_message)
        kw_args['status'] = _(self.status)
        kw_args['status_button'] = _(self.status_button)
        kw_args['form_title'] = _(self.form_title)
        return kw_args

    def get_form_kwargs(self, *args, **kwargs):
        kw_args = super(PersonFormMixin, self).get_form_kwargs(*args, **kwargs)
        kw_args['account'] = self.account
        return kw_args

    def get_template_names(self):
        template_name = super(PersonFormMixin, self).get_template_names()
        if self.request.is_ajax():
            return [self.modal_template_name]
        else:
            return template_name
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.account = get_object_or_404(Account, user=self.request.user)
        return super(PersonFormMixin, self).dispatch(*args, **kwargs)

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

class PersonCreate(AjaxableResponseMixin, PersonFormMixin, CreateView):
    """
    The create form view
    """
    status = 'create'
    status_button = "Add Person"
    form_title = "Add a Reservation"
    success_url = reverse_lazy('rsvp-initial')
    post_url = reverse_lazy('rsvp-create')

    def get(self, request):
        get = request.GET.copy()
        self.object = None
        try:
            reservations = get['reservations']
            filled_spots = get['filled_spots']
        except KeyError:
            reservations = self.account.reservations
            filled_spots = Person.objects.filter(account=self.account).count()
        if filled_spots < reservations:
            form = self.form_class(self.account)
        else:
            form = None
        context_dict = self.get_context_data(form=form)
        return self.render_to_response(context_dict)

class PersonUpdate(ModifyMixin, AjaxableResponseMixin, PersonFormMixin, UpdateView):
    """
    The update form view
    """
    status = "update"
    status_button = "Update"
    form_title = "Update a Reservation"
    success_url = reverse_lazy('rsvp-initial')

    def get_initial(self):
        self.person = get_object_or_404(Person, pk=self.kwargs[self.pk_url_kwarg])
        p = self.person
        initial = {
                'first_name': p.first_name,
                'last_name': p.last_name,
                'dietary_concerns': p.dietary_concerns,
                'email': p.email,
                'updates': p.updates,
                }
        return initial

class PersonDelete(ModifyMixin, AjaxableResponseMixin, DeleteView):
    """
    The delete form view
    """
    model = Person
    template_name = "rsvp/person_confirm_delete_modal.html"
    success_url = reverse_lazy('rsvp-initial')
    status = "delete"
    form_title = "Delete a Reservation"
    form_message = "Are you sure you want to delete this reservation?"

    def get_context_data(self, *args, **kwargs):
        kw_args = super(PersonDelete, self).get_context_data(*args, **kwargs)
        kw_args['form_title'] =  _(self.form_title)
        kw_args['form_message'] = _(self.form_message)
        return kw_args

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonDelete, self).dispatch(*args, **kwargs)

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
