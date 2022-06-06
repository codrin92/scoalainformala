from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
import mimetypes
import os
from django.http.response import HttpResponse

from Application1.models import Reporting

from Application1.mailmergerunner import mailmergefunction_quotes

from Application1.mailmergerunner import mailmergefunction_reports

class ProjectsView(LoginRequiredMixin, ListView):
    model = Reporting
    template_name = 'Application1/projects_index.html'
    paginate_by = 5
    queryset = model.objects.filter(active=1)
    context_object_name = 'projects'

    def get_context_data(self, *args, **kwargs):
        data=super(ProjectsView, self).get_context_data()
        # data['reporting_list'] = self.model.objects.filter(active=1)
        return data

class ProjectsClosedView(LoginRequiredMixin, ListView):
    model = Reporting     #Este modelul declarat in models.py
    template_name = 'Application1/projects_index.html'
    paginate_by = 5
    queryset = model.objects.filter(active=0)
    context_object_name = 'projects'

    def get_context_data(self, *args, **kwargs):
        data=super(ProjectsClosedView, self).get_context_data(*args, **kwargs)
        # data['reporting_list'] = self.model.objects.filter(active=0)
        return data

class CreateProjectsView(LoginRequiredMixin, CreateView):
    model = Reporting
    fields = ['project_name', 'project_address', 'project_value', 'client_company', 'client_representative', 'building_height', 'building_type', 'number_of_stairs']
    template_name ='Application1/project_form.html'
    counter = 1

    def get_success_url(self):
        self.counter += 1
        return reverse('reportwriter:project_list')

class UpdateProjectsView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Reporting
    fields = ['project_name', 'project_address', 'project_value', 'client_company', 'client_representative', 'building_height', 'building_type', 'number_of_stairs']
    template_name ='Application1/project_form.html'

    def get_success_url(self):
        return reverse('reportwriter:project_list')

    def test_func(self):                             #de facut la toate
        if self.request.user.is_authenticated:
            return True
        return False

class AssignEngineerView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Reporting
    fields = ['assigned_engineer']
    template_name = 'Application1/assign_engineer.html'

    def get_success_url(self):
        return reverse('reportwriter:project_list')

    def test_func(self):                             #de facut la toate
        if self.request.user.is_authenticated:
            return True
        return False

@login_required
def delete_project(request, pk):
    Reporting.objects.filter(id=pk).update(active=0)
    return redirect('reportwriter:project_list')

@login_required
def activate_project(request, pk):
    Reporting.objects.filter(id=pk).update(active=1)
    return redirect('reportwriter:project_list')

@login_required
def run_quote(request, pk):
    Reporting.objects.filter(id=pk).update(quote_produced=1)
    project_specifics=Reporting.objects.get(id=pk)
    mailmergefunction_quotes(project_specifics, pk)
    return redirect('reportwriter:project_list')

@login_required
def download_quote(request, pk):
# def download_report(request, pk):
#     Reporting.objects.filter(id=pk)
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    project_specifics=Reporting.objects.get(id=pk)
    filename = f"Q{pk}-{project_specifics.project_name}.pdf"
    # filename = 'template.docx'
    # Define the full file path
    filepath = BASE_DIR + '/templates/Application1/testfiles/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # path = open(filepath, 'r', encoding="utf8")
    # Set the mime type
    # mime_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    # mime_type="application/pdf"
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # response['Content-Encoding'] = 'UTF-8'
    # response['Content-Length'] = len(path)
    # response['Errors']= 'ignore'
    # Return the response value
    Reporting.objects.filter(id=pk).update(quote_issued=1)
    # redirect('reportwriter:project_list')
    return response

@login_required
def dl_and_refresh(request, pk):
    download_quote(request, pk)
    return redirect('reportwriter:project_list')

@login_required
def quote_accepted(request, pk):
    Reporting.objects.filter(id=pk).update(quote_accepted=1)
    return redirect('reportwriter:project_list')

@login_required
def generate_report(request, pk):
    Reporting.objects.filter(id=pk).update(report_generated=1)
    project_specifics = Reporting.objects.get(id=pk)
    mailmergefunction_reports(project_specifics, pk)
    return redirect('reportwriter:project_list')

@login_required
def download_report(request, pk):
    #     Reporting.objects.filter(id=pk)
    # Define Django project base directory
    Reporting.objects.filter(id=pk).update(report_issued=1)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    project_specifics=Reporting.objects.get(id=pk)
    filename = f"PRJ{pk}-{project_specifics.project_name}.pdf"
    # filename = 'template.docx'
    # Define the full file path
    filepath = BASE_DIR + '/templates/Application1/testfiles/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # path = open(filepath, 'r', encoding="utf8")
    # Set the mime type
    # mime_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    # mime_type="application/pdf"
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # response['Content-Encoding'] = 'UTF-8'
    # response['Content-Length'] = len(path)
    # response['Errors']= 'ignore'
    # Return the response value
    return response







