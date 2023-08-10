from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,reverse
from django.views import generic
from .models import Agent
from .models import LeadModel
from .forms import LeadModelForm


class Home(generic.TemplateView):
    template_name = 'leads/home.html'


class LeadList(generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset = LeadModel.objects.all()
    context_object_name = 'leads'


class LeadDetailView(generic.DetailView):
    template_name = 'leads/lead-detail.html'
    queryset = LeadModel.objects.all()
    context_object_name = 'lead'


class LeadCreateView(generic.CreateView):
    template_name = 'leads/lead-create.html'
    form_class = LeadModelForm
    success_url = '/leads/list'


class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/lead-update.html'
    queryset = LeadModel.objects.all()
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse('leads:lead-list')