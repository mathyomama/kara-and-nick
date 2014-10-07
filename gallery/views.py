from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from instagram.client import InstagramAPI


CLIENT_ID = 'dc7aff00c8904bb59730839bcb7c9f02'
CLIENT_SECRET = 'cffd09d1e717408abfa2b4c7a8f6e0d1' 
TAG = "kardoswedding"
# image dict keys
#['caption', 'tags', 'comments', 'filter', 'created_time', 'comment_count', 'like_count', 'link', 'likes', 'images', 'type', 'id', 'user']

@login_required
def index(request):
    context = RequestContext(request)
    context_dict = dict()
    api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    
    pictures_with_tag = api.tag_recent_media(tag_name="diaosmith")
    pictures_with_tag = pictures_with_tag[0]
    pic_urls = []
    context_dict['pictures_with_tag'] = pictures_with_tag
    for pic in pictures_with_tag:
        pic_urls.append((pic.images['standard_resolution']. url,pic.caption.text))
    context_dict['pic_list'] = pic_urls 
    return render_to_response('gallery.html', context_dict, context)
