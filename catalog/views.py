from django.shortcuts import render
from datetime import datetime
import requests

# Create your views here.

def index(request):
    return render(request,
                  'index.html',                  # template
                  {'now' : str(datetime.now())}  # Context
                 )


def country_info(request):
    if 'code' in request.POST:
        # get info about country and send info to template
        code = request.POST['code']
        resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
        if resp.status_code == 200:
            info = resp.json()
            return render(request,'country.html',
                          {'info': info, 'code' : code})
        else:
            return render(request, 'country.html',
                          {'error': 'Country not found!','code' : code })
    else:
        return render(request, 'country.html')