from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import OurStoryEntry

@login_required
def index(request):
    context = RequestContext(request)
    context_dict = dict()
    our_story_entries = OurStoryEntry.objects.all()
    context_dict['our_story_entries'] = our_story_entries

    return render_to_response('our_story.html', context_dict, context)
