from django.shortcuts import render
from django.views import generic
from .models import LeadModel


class Home(generic.TemplateView):
    template_name = 'leads/home.html'


class LeadList(generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset = LeadModel.objects.all()
    context_object_name = 'leads'