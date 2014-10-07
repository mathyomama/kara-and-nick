from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import ItineraryEntry, WhatToExpect

@login_required
def index(request):
    context = RequestContext(request)
    context_dict = dict()
    itinerary_entries = ItineraryEntry.objects.all()
    what_to_expect_entries = WhatToExpect.objects.all()
    context_dict['what_to_expect_entries'] = what_to_expect_entries
    context_dict['itinerary_entries'] = itinerary_entries 
    return render_to_response('the_big_day.html', context_dict, context)
