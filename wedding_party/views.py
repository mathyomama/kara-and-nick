from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import PartyMember 

# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = dict()
    party_members = PartyMember.objects.all()

    party_member_labels = list(PartyMember.RESPONSIBILITIES)
    all_but_last = []
    for i in party_member_labels:
        if i != (None,"Responsibility"):
            all_but_last.append(i)
        
    context_dict['responsibilities'] = all_but_last
    context_dict['party_members'] = party_members
    return render_to_response('wedding_party.html', context_dict, context)
