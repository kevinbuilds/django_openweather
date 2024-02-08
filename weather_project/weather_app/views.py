from django.shortcuts import render
import datetime
import requests

# Create your views here.
def index(request):
    API_KEY = open("../API_KEY.txt", "r").read()
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"
    forecast_url = "https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&units=metric&appid={}"

    if request.method == "POST":
        city1 = request.POST.get('city1',None)
        #city2 = request.POST.get('city2', None)

        # weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_url)

        if city1:
            weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_url)

        else:
            weather_data1, daily_forecasts1 = None, None

        context = {
            "weather_data1": weather_data1,
            "daily_forecasts1": daily_forecasts1,
        }

        return render(request, "weather_app/index.html", context)

    else:
        return render(request, "weather_app/index.html")

def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    lat, lon = response['coord']['lat'], response['coord']['lon']
    forecast = requests.get(forecast_url.format(lat, lon, api_key)).json()

    weather_data = {
            "city": city,
            "min_temp": round(response['main']['temp']),
            "description": response['weather'][0]['description'],
            "icon": response['weather'][0]['icon']
        }

    daily_forecasts = []
    for daily_data in forecast['daily'][:5]:
        daily_forecasts.append(
                {
                    "day": datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
                    "min_temp": round(daily_data['temp']['min']),
                    "max_temp": round(daily_data["temp"]["max"]),
                    "description": daily_data['weather'][0]["description"],
                    "icon": daily_data['weather'][0]['icon']
                }
            )

    return weather_data, daily_forecasts