from typing import Any, Dict
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render,reverse
from django.views import generic
from .models import Agent
from .models import LeadModel,Category
from .forms import LeadModelForm,CustomUserCreationForm,AssignAgentForm,LeadCategoryUpdate
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
    context_object_name = 'leads'
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = LeadModel.objects.filter(organization=user.userprofile,agent__isnull=False)
        else:
            queryset = LeadModel.objects.filter(organization=user.agent.organization,agent__isnull=False)
            queryset = queryset.filter(agent__user=user)
        return queryset
    def get_context_data(self,**kwargs):
        context = super(LeadList,self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organisor:
            queryset = LeadModel.objects.filter(organization=user.userprofile,agent__isnull=True)
            context.update({
                "unassigned_leads":queryset
            })
        return context

class LeadDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'leads/lead-detail.html'
    def get_queryset(self):
        user = self.request.user
        return LeadModel.objects.filter(organization=user.userprofile)
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
    def get_queryset(self):
        user = self.request.user
        return LeadModel.objects.filter(organization=user.userprofile)
    context_object_name = 'lead'
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse('leads:lead-list')
    
class LeadDeleteView(OrganisorLoginRequiredMixin,generic.DeleteView):
    template_name = 'leads/lead-delete.html'
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = LeadModel.objects.filter(organization=user.userprofile)
        else:
            queryset = LeadModel.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=user)
        return queryset
    def get_success_url(self):
        return reverse('leads:lead-list')
    

class AssignAgentView(OrganisorLoginRequiredMixin,generic.FormView):
    template_name = 'leads/assign-agent.html'
    form_class = AssignAgentForm
    def get_success_url(self):
        return reverse('leads:lead-list')
    
    def get_form_kwargs(self,**kwargs):
        kwargs = super(AssignAgentView,self).get_form_kwargs(**kwargs)
        kwargs.update({
            'request':self.request
        })
        return kwargs
    def form_valid(self,form):
        agent = form.cleaned_data['agent']
        lead = LeadModel.objects.get(id=self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView,self).form_valid(form)
    

class CategoryListView(LoginRequiredMixin,generic.ListView):
    template_name = 'leads/category-list.html'
    context_object_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView,self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organisor:
            queryset = LeadModel.objects.filter(organization=user.userprofile)
        else:
            queryset = LeadModel.objects.filter(organization=user.agent.organization)
        context.update({
            'unassigned_lead_count':queryset.filter(category__isnull=True).count()
        })
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset
    

class CategoryDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'leads/category-detail.html'
    context_object_name = 'category'
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset
    

class LeadCategoryUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'leads/category-update.html'
    context_object_name = 'lead'
    form_class = LeadCategoryUpdate
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = LeadModel.objects.filter(organization=user.userprofile)
        else:
            queryset = LeadModel.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_success_url(self):
        return reverse('leads:lead-detail',kwargs={'pk':self.get_object().id })