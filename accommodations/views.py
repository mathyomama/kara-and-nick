from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import AccommodationsEntry

@login_required
def index(request):
    context = RequestContext(request)
    context_dict = dict()

    context_dict['accommodations'] = AccommodationsEntry.objects.all()

    return render_to_response('accommodations.html', context_dict, context)
