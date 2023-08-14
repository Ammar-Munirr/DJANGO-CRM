from django.http import HttpResponse
from django.core.mail import send_mail
import random
from django.shortcuts import render,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentForm
from .mixins import OrganisorLoginRequiredMixin


class AgentListView(OrganisorLoginRequiredMixin,generic.ListView):
    template_name = 'agents/agent-list.html'
    context_object_name = 'agents'
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    
class AgentCreateView(OrganisorLoginRequiredMixin,generic.CreateView):
    template_name = 'agents/agent-create.html'
    form_class = AgentForm
    def get_success_url(self):
        return reverse('agents:agent-list')
    def form_valid(self,form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(str(random.randint(0,10000)))
        user.save()
        Agent.objects.create(
            user=user,
            organization = self.request.user.userprofile
        )
        send_mail(
            subject='You have been invited as agent',
            message='You have been added as agent in CRM. Please Come Login to start.',
            from_email='ammar@crm.com',
            recipient_list=['user@crm.com']
        )
        return super(AgentCreateView,self).form_valid(form)
    
class AgentDetailView(OrganisorLoginRequiredMixin,generic.DetailView):
    template_name = 'agents/agent-detail.html'
    context_object_name = 'agent'
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    
class AgentUpdateView(OrganisorLoginRequiredMixin,generic.UpdateView):
    template_name = 'agents/agent-update.html'
    form_class = AgentForm
    context_object_name = 'agent'
    def get_queryset(self):
        return Agent.objects.all()
    def get_success_url(self):
        return reverse('agents:agent-list')
    
class AgentDeleteView(OrganisorLoginRequiredMixin,generic.DeleteView):
    template_name = 'agents/agent-delete.html'
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    def get_success_url(self):
        return reverse('agents:agent-list')