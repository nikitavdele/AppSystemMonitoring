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
            for idx, mhz_value in enumerate(cpu_mhz_value):
                dk[f'cpu_MHz{idx + 1}'] = mhz_value
            #dk['cpu_MHz1'] = cpu_mhz_value[0]
            # dk['cpu_MHz2'] = cpu_mhz_value[1]
            # dk['cpu_MHz3'] = cpu_mhz_value[2]
            # dk['cpu_MHz4'] = cpu_mhz_value[3]
            # dk['cpu_MHz5'] = cpu_mhz_value[4]
            # dk['cpu_MHz6'] = cpu_mhz_value[5]
            # dk['cpu_MHz7'] = cpu_mhz_value[6]
            # dk['cpu_MHz8'] = cpu_mhz_value[7]
        if 'cpu family' in ar_data[i]:
            value = ar_data[i + 1].strip().split()[0]
            cpu_family_value.append(value)
            dk['cpu family'] = cpu_family_value
        if 'cpu cores' in ar_data[i]:
            dk['cpu_cores'] = ar_data[i+1].strip().split()[0]

    with open('cpuLoad', 'r', encoding='utf-8') as f:
        data = f.read()

    load_data = data.split()
    dk['load_1min'] = load_data[0]
    dk['load_5min'] = load_data[1]
    dk['load_15min'] = load_data[2]

    # loadavg_values = [float(parts[i]) for i in range(3)]
    # dk['loadavg'] = loadavg_values

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

    with open('HDD', 'r', encoding='utf-8') as f:
        data = f.readlines()

    disk_data = []
    for line in data[1:]:
        parts = line.split()
        dk['filesystem'] = parts[0]
        dk['disk_size'] = parts[1]
        dk['disk_used'] = parts[2]
        dk['disk_free'] = parts[3]
        dk['disk_used_percent'] = parts[4]
        dk['mount_point'] = parts[5]

    return HttpResponse(json.dumps(dk))


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")