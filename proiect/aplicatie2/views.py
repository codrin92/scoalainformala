from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie2.models import Companies


class CompaniesView(LoginRequiredMixin, ListView):
    model = Companies     #Este modelul declarat in models.py
    template_name = 'aplicatie2/company_form.html'

    def get_context_data(self, *args, **kwargs):
        data=super(CompaniesView, self).get_context_data()
        data['companies_list'] = self.model.objects.filter(active=1)
        return data

class CreateCompaniesView(LoginRequiredMixin, CreateView):
    model = Companies
    # fields = '__all__'
    fields = ['name', 'company_type', 'website', 'active']
    template_name = 'aplicatie2/company_form_base.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')

class UpdateCompaniesView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = ['name', 'company_type', 'website', 'active']
    template_name = 'aplicatie2/company_form_base.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')

def delete_company(request, pk):
    Companies.objects.filter(id=pk).update(active=0)
    return redirect('companies:lista_companii')

def activate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:lista_companii')

class CompaniesInactiveView(LoginRequiredMixin, ListView):
    model = Companies     #Este modelul declarat in models.py
    template_name = 'aplicatie2/company_form.html'

    def get_context_data(self, *args, **kwargs):
        data=super(CompaniesInactiveView, self).get_context_data(*args, **kwargs)
        data['companies_list'] = self.model.objects.filter(active=0)
        return data