from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from . models import City,CityUser

# Create your views here.


def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0d99bc7236ea511b6b03459e7e2505f7'

    a = request.user.is_authenticated
    if a:
        if request.method=='POST':
            try:
                city = request.POST["name"]
                r = requests.get(url.format(city)).json()
                c=(r["main"]["temp"]-32)*(5/9)

            except:
                messages.error(request,'Sorry! location is not found,Please! try other location')
                return HttpResponseRedirect("")

            form = CityForm(request.POST)
            if form.is_valid():
                new = CityUser(name=form.cleaned_data["name"],user_name=request.user)
                new.save()


        form = CityForm()
        cityuser = CityUser.objects.all().order_by("-pub_date")
        #cities = City.objects.all().order_by("-pub_date")
        cities = cityuser.filter(user_name=request.user)
        weather_data = []
        for city in cities:
            r = requests.get(url.format(city)).json()
            c=(r["main"]["temp"]-32)*(5/9)
            c=round(c,2)

            city_weather = {
                'city':city.name,
                'temperature':c,
                'description':r["weather"][0]["description"],
                'icon':r["weather"][0]["icon"],
            }
            weather_data.append(city_weather)
        #print(weather_data)

    else:
        if request.method=='POST':
            try:
                city = request.POST["name"]
                r = requests.get(url.format(city)).json()
                c=(r["main"]["temp"]-32)*(5/9)

            except:
                messages.error(request,'Sorry! location is not found,Please! try other location')
                return HttpResponseRedirect("")

            form = CityForm(request.POST)
            if form.is_valid():
                new = City(name=form.cleaned_data["name"],user_name=request.user)
                new.save()


        form = CityForm()

        cities = City.objects.all().order_by("-pub_date")
        weather_data = []
        for city in cities:
            r = requests.get(url.format(city)).json()
            c=(r["main"]["temp"]-32)*(5/9)
            c=round(c,2)

            city_weather = {
                'city':city.name,
                'temperature':c,
                'description':r["weather"][0]["description"],
                'icon':r["weather"][0]["icon"],
            }
            weather_data.append(city_weather)
        #print(weather_data)
    context = {'weather_data':weather_data,'form':form}


    return render(request,'weatherapp/home.html',context)


'''def delete(request,id):
    city = get_object_or_404(CityUser,pk=id)
    city.delete()
    return redirect('home')'''
