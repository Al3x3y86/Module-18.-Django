from django.shortcuts import render
from django.views.generic import TemplateView


def class_view(request):
    return render(request, 'second_task/class_view.html')

def function_view(request):
    return render(request, 'second_task/function_view.html')


