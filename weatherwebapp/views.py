from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests
import datetime

def index(request):
    return render(request, 'weatherwebapp/login.html')

def register(request):
    return render(request, 'weatherwebapp/register.html')

def profile(request):
    return render(request, 'weatherwebapp/profile.html')

def test_request(request):
    response = requests.get('https://api.darksky.net/forecast/950c63fab35d31f7fea2bc4a165c5bf2/-7.797068,110.370529?extend=hourly')
    weather = response.json()
    schedule = [
        ['10:00', 'Monday'],
        ['13:00', 'Monday'],
        ['16:00', 'Monday'],
        ['10:00', 'Tuesday'],
        ['15:00', 'Wednesday'],
        ['15:00', 'Thursday'],
        ['15:00', 'Friday']
    ]
    timestamp_list = []
    weather_list = []
    for hourly in weather['hourly']['data']:
        hourly_timestamp = hourly['time']
        summary = hourly['summary']
        date = datetime.datetime.fromtimestamp(float(hourly_timestamp))
        day_name = date.strftime("%A")
        hour = date.strftime("%R")
        for single_sched in schedule:
            if single_sched[0] == hour:
                if single_sched[1] == day_name:
                    timestamp_list.append(hourly_timestamp)
                    weather_list.append(summary)
    return render(request, 'weatherwebapp/test_request.html', {
        'timestamp': timestamp_list,
        'weather': weather_list
    })

