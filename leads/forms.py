from django import forms
from .models import LeadModel


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = LeadModel
        fields = '__all__'