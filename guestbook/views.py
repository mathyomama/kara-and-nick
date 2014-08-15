from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = RequestContext(request)
    context_dict = dict()

    posts = Guestbook.objects.all()#.order_by("-created")
	
    #paginator = Paginator(posts, 2)

    context_dict['apple']=request.user
    context_dict['posts']=posts	
    context_dict['ba']="NOWAY"
		
    return render_to_response("guestbook.html", context_dict, context)

