from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import requests


# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=19e314a02c78c1106c28037fcf77f454'
    city = 'Dubai'
    r = requests.get(url.format(city)).json()
    # r=url.format(city)
    # print(r.text)
    weather_data = {'city': city,
                    'temperature': r['main']['temp'],
                    'description': r['weather'][0]['description'],
                    'icon': r['weather'][0]['icon'],
                    }
    print(weather_data)
    return render(request, 'index.html', {'weather_data': weather_data})
