from django import forms
from leads.models import Agent



class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['user']