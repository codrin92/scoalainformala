from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, TemplateView

class CreateHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home_page.html'

