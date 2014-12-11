from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import OurStoryEntry

@login_required
def index(request):
    context = RequestContext(request)
    context_dict = dict()
    our_story_entries = OurStoryEntry.objects.all()
    order = ["How did you meet?", "First impression", "First date", "First kiss","The proposal", "Mystery question 1"]
    sorted_our_story_entries = []
    for question in order:
        for entry in our_story_entries:
                if entry.question == question:
                    sorted_our_story_entries.append(entry)
    context_dict['our_story_entries'] = sorted_our_story_entries

    return render_to_response('our_story.html', context_dict, context)
