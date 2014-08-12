from django.shortcuts import render, render_to_response
from django.template import RequestContext
import yweather
from .models import Welcome
from .models import WelcomeUpdateEntry

# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = dict()
    greeting = Welcome.objects.all()
    context_dict['greeting'] = greeting[0]
    update_entries = WelcomeUpdateEntry.objects.all()
    context_dict['updates'] = update_entries

    weather_client = yweather.Client()
    bayanihan_woeid = weather_client.fetch_woeid("Tampa, Florida 33626")
    weather_dict = weather_client.fetch_weather(bayanihan_woeid)
    weather_forecast = weather_dict['forecast']
    context_dict['weather'] = weather_forecast


    return render_to_response('welcome.html', context_dict, context)
