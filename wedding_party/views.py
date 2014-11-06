from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import PartyMember 

# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = dict()
    party_members = PartyMember.objects.all()
    for member in party_members:
        member.name = member.name.replace(' ','<br>')
    party_member_labels = list(PartyMember.RESPONSIBILITIES)

    party_member_label_groupings = [[("MAID_OF_HONOR", "Maid of<br>Honor",4,12,4), ("MATRON_OF_HONOR","Matron of<br>Honor",4,12,4), ("BEST_MAN","Best<br>Man",4,12,4)], [("BRIDESMAID", "Bridesmaids",12,6,6)],[("JR_BRIDESMAID", "Junior Bridesmaids",12,6,6)],[("GROOMSMAN","Groomsmen",12,6,6)],[("RING_BEARER","Ring<br>Bearer",4,12,4), ("COIN_BEARER","Coin<br>Bearer",4,12,4),("FLOWER_GIRL", "Flower<br>Girl",4,12,4)]]
    all_but_last = []
    for i in party_member_labels:
        if i != (None,"Responsibility"):
            all_but_last.append(i)
        
    context_dict['responsibilities'] = all_but_last
    context_dict['party_member_label_groupings'] = party_member_label_groupings
    context_dict['party_members'] = party_members
    return render_to_response('wedding_party.html', context_dict, context)
