from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from Application1.models import Reporting

class ReportsView(ListView):
    model =  Reporting
    template_name = 'Application1/projects_index.html'

class CreateReportsView(CreateView):
    model = Reporting
    fields = ['project_name', 'project_address', 'project_value', 'client', 'building_height', 'building_type', 'number_of_stairs']
    template_name ='Application1/project_form.html'

    def get_success_url(self):
        return reverse('reportwriter:lista_rapoarte')

class UpdateReportsView(UpdateView):
    model = Reporting
    fields = ['project_name', 'project_address', 'project_value', 'client', 'building_height', 'building_type', 'number_of_stairs']
    template_name ='Application1/project_form.html'

    def get_success_url(self):
        return reverse('reportwriter:lista_rapoarte')

