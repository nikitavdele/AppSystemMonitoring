from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm
from django.http import JsonResponse
import json


# def index(request):
#     x=2**1000
#
#     return HttpResponse(request, 'DjangoFirstProject/index.html',"<h2>Главная</h2>",{"x":x})


# def index(request):
#     return HttpResponse("<h2>Главная</h2>")

# def index(request):
#     userform = UserForm()
#     return render(request, "DjangoFirstProject/index.html", {"form": userform})

from django.http import JsonResponse
import json
import re

def index(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get("name")
        age = request.POST.get("age")
        comment = request.POST.get("comment")
        response_data = {
            'message': f"Привет, {name}. Твой возраст: {age}. Дополнительный комментарий: {comment}"
        }
        return JsonResponse(response_data)
    else:
        userform = UserForm()
        return render(request, "DjangoFirstProject/index.html", {"form": userform})


def about(request, name, age):
    return HttpResponse(f"""
            <h2>О разработчике</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)


def get_params(request):
    with open('cpuMHz', 'r', encoding='utf-8') as f:
        data = f.read()
    # print(data)
    # print(data.split(':'))
    dk = {}
    ar_data = data.split(':')
    cpu_mhz_value=[]
    cpu_family_value=[]

    for i in range(len(ar_data)):
        if 'cpu MHz' in ar_data[i]:
            value = ar_data[i + 1].strip().split()[0]
            cpu_mhz_value.append(value)
            dk['cpu MHz'] = cpu_mhz_value
        if 'cpu family' in ar_data[i]:
            value = ar_data[i + 1].strip().split()[0]
            cpu_family_value.append(value)
            dk['cpu family'] = cpu_family_value
        if 'cpu cores' in ar_data[i]:
            dk['cpu cores'] = ar_data[i+1].strip().split()[0]

    with open('cpuLoad', 'r', encoding='utf-8') as f:
        data = f.read()

    parts = data.split()
    loadavg_values = [float(parts[i]) for i in range(3)]
    dk['loadavg'] = loadavg_values

    with open('RAM', 'r', encoding='utf-8') as f:
        data = f.read()

    partsRAM = data.split(':')
    for i in range(len(partsRAM)):
        if 'MemTotal' in partsRAM[i]:
            dk['MemTotal'] = partsRAM[i+1].strip().split()[0]
        if 'MemFree' in partsRAM[i]:
            dk['MemFree'] = partsRAM[i+1].strip().split()[0]
        if 'MemAvailable' in partsRAM[i]:
            dk['MemAvailable'] = partsRAM[i+1].strip().split()[0]
        if 'SwapTotal' in partsRAM[i]:
            dk['SwapTotal'] = partsRAM[i+1].strip().split()[0]


    return HttpResponse(json.dumps(dk))

# def get_params(request):
#     with open('cpu', 'r', encoding='utf-8') as f:
#         data = f.read()
#         # print(data)
#     # print(data.split(':'))
#     dk = {}
#     ar_data = data.split(':')
#     for i in range(len(ar_data)):
#         print(ar_data[i].strip())
#         if ar_data[i].strip() == 'cpu_MHz':
#             dk['cpu_MHz'] = ar_data[i+1].strip()
#     return HttpResponse(json.dumps(dk))

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")