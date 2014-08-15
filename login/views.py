from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



def index(request):
    context = RequestContext(request)
    context_dict = dict()
    
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponseRedirect(request.GET['next'])
        else:
            # Return an 'invalid login' error message.
            # This scenario would most likely be a HTTP GET.
            return HttpResponse("Invalid login details supplied.")
    return render_to_response('login.html', context_dict, context)
