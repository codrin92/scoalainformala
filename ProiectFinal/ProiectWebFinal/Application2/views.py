from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
import mimetypes
import os
from django.http.response import HttpResponse

# from Application2.models import Revenues

from Application1.models import Reporting

from Application1.mailmergerunner import mailmergefunction_invoices


class ForwardRevenuesView(LoginRequiredMixin, ListView):
    model = Reporting
    template_name = 'Application2/forward_revenue_index.html'
    # paginate_by = 5
    # # queryset = model.objects.filter(active=1)
    # context_object_name = 'revenues'

    def get_context_data(self, *args, **kwargs):
        data=super(ForwardRevenuesView, self).get_context_data()
        data['reporting_list'] = self.model.objects.filter(quote_accepted =1, report_generated=0)
        return data

class DoneRevenuesView(LoginRequiredMixin, ListView):
    model = Reporting
    template_name = 'Application2/done_revenue_index.html'
    # paginate_by = 5
    # # queryset = model.objects.filter(active=1)
    # context_object_name = 'revenues'

    def get_context_data(self, *args, **kwargs):
        data=super(DoneRevenuesView, self).get_context_data()
        data['reporting_list'] = self.model.objects.filter(report_generated=1)
        return data

class ReassignEngineerView(LoginRequiredMixin, UpdateView):
    model = Reporting
    fields = ['assigned_engineer']
    template_name = 'Application1/assign_engineer.html'

    def get_success_url(self):
        return reverse('finance:revenues_list')

@login_required
def generate_invoice(request, pk):
    Reporting.objects.filter(id=pk).update(invoice_generated=1)
    project_specifics = Reporting.objects.get(id=pk)
    mailmergefunction_invoices(project_specifics, pk)
    return redirect('finance:completed_work')

@login_required
def download_invoice(request, pk):
    #     Reporting.objects.filter(id=pk)
    # Define Django project base directory
    Reporting.objects.filter(id=pk).update(invoice_issued=1)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    project_specifics=Reporting.objects.get(id=pk)
    filename = f"INV{pk}.pdf"
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
