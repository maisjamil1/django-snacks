from django.shortcuts import render
#Create home view
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'hello-home.html'


