from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render,reverse
from django.views import generic
from .models import Agent
from .models import LeadModel
from .forms import LeadModelForm,CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganisorLoginRequiredMixin



class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    def get_success_url(self):
        return reverse('login')

class Home(generic.TemplateView):
    template_name = 'leads/home.html'

class LeadList(LoginRequiredMixin,generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset = LeadModel.objects.all()
    context_object_name = 'leads'

class LeadDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'leads/lead-detail.html'
    queryset = LeadModel.objects.all()
    context_object_name = 'lead'

class LeadCreateView(OrganisorLoginRequiredMixin,generic.CreateView):
    template_name = 'leads/lead-create.html'
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse('leads:lead-list')
    def form_valid(self,form):
        send_mail(
            subject='LEAD CREATED',
            from_email='ammar@crm.com',
            recipient_list=['user@crm.com'],
            message='Your Lead has Been created go to the site to see the leads.'
        )
        return super(LeadCreateView,self).form_valid(form)

class LeadUpdateView(OrganisorLoginRequiredMixin,generic.UpdateView):
    template_name = 'leads/lead-update.html'
    queryset = LeadModel.objects.all()
    context_object_name = 'lead'
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse('leads:lead-list')
    
class LeadDeleteView(OrganisorLoginRequiredMixin,generic.DeleteView):
    template_name = 'leads/lead-delete.html'
    queryset = LeadModel.objects.all()
    def get_success_url(self):
        return reverse('leads:lead-list')