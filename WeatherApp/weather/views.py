from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def posts_list(request):
    app_id = 'c5000a2e98f4e93d4d87f5716d1f13db'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()    # for cleaning forms

    cities = City.objects.all()

    all_city = []

    for city in cities:
        r = requests.get(url.format(city.name)).json()    # get dict format
        city_data = {'city': city.name,
                     'temperature': r['main']['temp'],
                     'icon': r['weather'][0]['icon'],
                    }

        all_city.append(city_data)

    data = {'all_cities': all_city, 'form': form}

    return render(request, 'weather/index.html', data)
