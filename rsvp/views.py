from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def index(request):
    context = RequestContext(request)
    context_dict = dict()

    return render_to_response('rsvp.html', context_dict, context)
