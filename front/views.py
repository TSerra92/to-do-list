from datetime import datetime

import requests
from api.models import Task
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def form(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        descricao = request.POST["descricao"]
        local = request.POST["local"]
        data = request.POST["data"]
        hora = request.POST["hora"]

        info = {
            "nome": nome,
            "descricao": descricao,
            "local": local,
            "data": data,
            "hora": hora,
        }

        #print(info)

        r = requests.post('http://127.0.0.1:8000/api/create', data=info)
        #task = Task.objects.create()
    
    return render(request, 'form.html')

def list(request):
    response = requests.get('http://127.0.0.1:8000/api/')

    tasks = response.json()
    #print(tasks)

    return render(request, 'list.html', {'tasks': tasks})
