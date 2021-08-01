from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def index(request):
    country_covid_data = []
    global_covid_data  = {}
    background_colors  = ['success', 'danger', 'warning', 'info','primary', 'secondary']

    if request.method == "POST":
        user_entered_country = request.POST['country_name']
        user_entered_country = user_entered_country.lower()
        while len(country_covid_data) == 0:
            try:
                response = requests.get(f'https://api.covid19api.com/country/{user_entered_country}?from=2021-02-27T00:00:00Z&to=2021-03-01T00:00:00Z')
            except JSONDecodeError:
                continue
            else:
                country_covid_data = response.json()

    while len(global_covid_data) == 0:
        try:
            response = requests.get('https://api.covid19api.com/summary')
        except JSONDecodeError:
            continue
        else:
            global_covid_data = response.json()['Global']

    context = {
        'global_data': global_covid_data,
        'color': background_colors,
        'country_data': country_covid_data,
    }

    return render(request, 'index.html', context)
