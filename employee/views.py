from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from employee.forms import EmployersForm
from employee.models import Employers


class EmployersList(ListView):
    paginate_by = 50
    template_name = 'index.html'
    context_object_name = 'employers'
    model = Employers


class EmployersDeleteView(DeleteView):
    model = Employers

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, f"Удалино !")
        return reverse('employers')


class EmployersUpdateView(UpdateView):
    model = Employers
    template_name = 'update.html'
    form_class = EmployersForm
    context_key = 'employer_update'

    def get_success_url(self):
        messages.success(self.request, f"Сотрудник  {self.object.name}  обновлено !")
        return reverse('employers')


class EmployersCreateView(CreateView):
    template_name = 'create.html'
    model = Employers
    form_class = EmployersForm

    def get_success_url(self, *args):
        messages.success(self.request, f"Сотрудник  {self.object.name}  создано !")
        return reverse('employers')
