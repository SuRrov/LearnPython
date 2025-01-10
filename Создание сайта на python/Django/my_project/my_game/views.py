from django.shortcuts import render

# Create your views here.
import random
from django.http import HttpResponse

def game_view(request):
    numbers = [random.randint(0, 3) for _ in range(3)]
    if all(num == numbers[0] for num in numbers):
        return HttpResponse(f"Победа, все 3 числа равны!<br>Числа: {numbers}")
    else:
        return HttpResponse(f"Повезет в следующий раз!<br>Числа: {numbers}")