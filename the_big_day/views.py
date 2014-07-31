from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = dict()

    return render_to_response('the_big_day.html', context_dict, context)
