from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import requests
from .models import City
from .forms import CityCreateForm


# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=19e314a02c78c1106c28037fcf77f454'
    form = CityCreateForm()
    error_message = ''
    message = ''
    message_class = ''
    if request.method == "POST":
        form = CityCreateForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    error_message = 'Invalid City'
                    # print(error_message)
            else:
                error_message = 'City Already exists'
                # print(error_message)
        if error_message:
            message = error_message
            message_class = 'alert-danger'
            print(message)
        else:
            message = 'City Added Successfully'
            message_class = 'alert-success'
            print(message)

        # return HttpResponseRedirect("/")
    # else:
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=19e314a02c78c1106c28037fcf77f454'
    # new_city = ''
    form = CityCreateForm()
    data_city = City.objects.all()
    weather_data_list = []
    for city in data_city:
        # city = 'Dubai'
        r = requests.get(url.format(city)).json()
        # p = requests.get(url.format(city))
        # r=url.format(city)
       # 'print(p.dt)
        weather_data = {'city': city,
                        'temperature': r['main']['temp'],
                        'degreecelsius': round((r['main']['temp'] - 32) * 5 / 9, 2),
                        'humidity': r['main']['humidity'],
                        'description': r['weather'][0]['description'],
                        'icon': r['weather'][0]['icon'],
                        }
        weather_data_list.append(weather_data)

    # print(weather_data_list)
    return render(request, 'index.html', {'weather_data': weather_data_list,
                                          'form': form,
                                          'message': message,
                                          'message_class': message_class
                                          })


def delete(request, city_name):
    City.objects.filter(name=city_name).delete()
    return HttpResponseRedirect("/")
