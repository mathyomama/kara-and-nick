from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from yelpapi import YelpAPI
import folium
import datetime
import os.path
import time
from geopy.geocoders import GoogleV3

OSM_FILE = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
TOKEN = "" 
TOKEN_SECRET = "" 

variable_assignment_file = open('/home/kara-nick-wedding/secret_keys.dat')
variable_assignment_lines = variable_assignment_file.readlines()
for variable in variable_assignment_lines:
    exec(variable)
CATEGORIES = ["restaurants", "nightlife", "arts", "shopping", "active"]

def make_osm_page():
    context_dict = dict()
    geolocator = GoogleV3()
    businesses_dict = {}
    yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
    context_dict['business_dict'] = businesses_dict
    tampa_gps=[27.952, -82.466]
    map_osm = folium.Map(location=tampa_gps, zoom_start=13, tiles='Stamen Terrain', width="100%")
    for tag in CATEGORIES:
        yelp_response = yelp_api.search_query(term=tag, location='tampa, fl', sort=2, limit=10)
        businesses_dict[tag] = yelp_response['businesses']
        for business in yelp_response['businesses']:
            business_address= ', '.join(business['location']['display_address'])
            address, (latitude, longitude) = geolocator.geocode(business_address)
            map_osm.simple_marker(location=[latitude, longitude], popup=str("<a href='"+business['url']+"' target='_blank'>"+business['name']+"</a>"))
    #map_osm.lat_lng_popover()
    map_osm.create_map(path='/tmp/osm.html')
    return


@login_required
def index(request):
    # check if osm file exists
    if os.path.isfile(OSM_FILE):
        # if it does exist, get the time it was created
        file_created_tuple = datetime.date.fromtimestamp(os.path.getmtime(OSM_FILE))
        # get today's date
        today_tuple = datetime.date.today()
        # calculate difference between days
        day_difference = today_tuple - file_created_tuple
        # if it was created yesterday, then generate a new one
        if day_difference.days != 0:
            os.remove(OSM_FILE)
            make_osm_page()
    else:
        make_osm_page()
    source_file =  open(OSM_FILE)
    source_file_lines = source_file.readlines()
    source_file_html = ''.join(source_file_lines)
    source_file_html = source_file_html[source_file_html.find("<body>")+6:source_file_html.find("</body>")]
    source_file_html = source_file_html.replace("None","")
    context = RequestContext(request)
    context_dict = dict()
    context_dict['categories'] = CATEGORIES
    context_dict['source'] =  source_file_html 
    return render_to_response('things_to_do.html', context_dict, context)
