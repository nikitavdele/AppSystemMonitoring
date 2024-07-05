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


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")