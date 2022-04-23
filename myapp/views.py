import requests
from django.shortcuts import render


# Create your views here.
def home(request):
    url = 'http://157.90.220.39:2998/getData/Price'
    r = requests.post(url)
    data = r.json()
    return render(request, 'myapp/index.html', {'data': data['data']})
