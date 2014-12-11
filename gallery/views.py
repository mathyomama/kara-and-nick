from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from instagram.client import InstagramAPI


CLIENT_ID = 'dc7aff00c8904bb59730839bcb7c9f02'
CLIENT_SECRET = 'cffd09d1e717408abfa2b4c7a8f6e0d1' 
TAG = "baino_kardos"
# image dict keys
#['caption', 'tags', 'comments', 'filter', 'created_time', 'comment_count', 'like_count', 'link', 'likes', 'images', 'type', 'id', 'user']

@login_required
def index(request):
    context = RequestContext(request)
    context_dict = dict()
    api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

#    instagram_pictures_file = open('/home/kara-nick-wedding/igpics')
#    instagram_pictures_lines = instagram_pictures_file.readlines()
#    old_links = [link.strip() for link in instagram_pictures_lines]
#    old_links = list(set(old_links))
#    context_dict['old_links'] = old_links
    
    pictures_with_tag = api.tag_recent_media(tag_name=TAG)
    pictures_with_tag = pictures_with_tag[0]
    pic_urls = []
    context_dict['pictures_with_tag'] = pictures_with_tag
    for pic in pictures_with_tag:
        pic_urls.append((pic.images['standard_resolution'].url, pic.images['thumbnail'].url, pic.caption.text))
    #pic_urls = [pic for pic in pic_urls if pic[0] not in old_links]
    context_dict['pic_list'] = pic_urls
    context_dict['old_links'] = []
  
#    igpics_file_1 = open('/home/kara-nick-wedding/igpics','w')
#    igpics_file_2 = open('/tmp/igpics','w')
#    everything = old_links
#    everything.extend(pic_urls[:][0])
#    try:
#        for i in everything:
#            if i.find("http") != -1:
#                url = i.strip()
#                igpics_file_1.write(url)
#                igpics_file_1.write('\n')
#                igpics_file_2.write(url)
#                igpics_file_2.write('\n')
#    except Exception as e:
#        print "hi"

    return render_to_response('gallery.html', context_dict, context)
