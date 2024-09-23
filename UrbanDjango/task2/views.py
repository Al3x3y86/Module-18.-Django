from django.shortcuts import render
from django.views.generic import TemplateView


class ClassView(TemplateView):
    template_name = 'second_task/class_template.html'


class FunctionView(TemplateView):
    template_name = 'second_task/func_template.html'
