from django.shortcuts import render

from django.views.generic import View,TemplateView,ListView,DeleteView,DetailView,CreateView,UpdateView
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy

# Create your views here.
class indexView(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]="hello All"
        return context


class SchoolList(ListView):
    model=models.school


class schoolDetailview(DetailView):

    context_object_name='school_details'
    model=models.school
    template_name="loginapp/school_detail.html"

class schoolCreateView(CreateView):
    fields=("name","principal","location")
    model=models.school
    success_url=reverse_lazy("loginapp:list")

class SchoolUpdateView(UpdateView):
    fields = ("name","principal","location")
    model = models.school
    success_url=reverse_lazy("loginapp:list")

class SchoolDeleteView(DeleteView):
    model = models.school
    success_url = reverse_lazy("loginapp:list")