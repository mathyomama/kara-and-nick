from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    context = RequestContext(request)
    context_dict = dict()
    
    # if they're submitting the login form
    if request.POST:
        # get the user input
        username = request.POST['username']
        password = request.POST['password']
        # check user input
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # check if we were sent to login from another page
            if request.GET:
                if request.GET['next']:
                    return HttpResponseRedirect(request.GET['next'])
                # if not just go to the welcome page
                else :
                    return HttpResponseRedirect('/welcome/')
            # if not just go to the welcome page
            else :
                return HttpResponseRedirect('/welcome/')
        else:
            # Return an 'invalid login' error message.
            # This scenario would most likely be a HTTP GET.
            return HttpResponse("Invalid login details supplied.")
    return render_to_response('login.html', context_dict, context)

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('')
