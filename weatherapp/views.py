from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import requests
from .models import City


# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=19e314a02c78c1106c28037fcf77f454'
    data_city = City.objects.all()
    weather_data_list = []
    for city in data_city:
        # city = 'Dubai'
        r = requests.get(url.format(city)).json()
        # p = requests.get(url.format(city))
        # r=url.format(city)
        # print(p.text)
        weather_data = {'city': city,
                        'temperature': r['main']['temp'],
                        'degreecelsius': round((r['main']['temp'] - 32) * 5 / 9, 2),
                        'humidity': r['main']['humidity'],
                        'description': r['weather'][0]['description'],
                        'icon': r['weather'][0]['icon'],
                        }
        weather_data_list.append(weather_data)
    print(weather_data_list)
    return render(request, 'index.html', {'weather_data': weather_data_list})
