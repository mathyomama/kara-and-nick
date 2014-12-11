from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import Contact

@login_required
def index(request):
    context = RequestContext(request)
    context_dict = dict()

    context_dict['contacts'] = Contact.objects.order_by('name')

    return render_to_response('contacts.html', context_dict, context)
