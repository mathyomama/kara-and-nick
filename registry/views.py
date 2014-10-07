from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import RegistryEntry

@login_required
def index(request):
    context = RequestContext(request)
    context_dict = dict()
    registry_entries = RegistryEntry.objects.all()
    context_dict['registry_entries'] = registry_entries
    return render_to_response('registry.html', context_dict, context)
