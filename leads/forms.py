from django import forms
from .models import LeadModel
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth import get_user_model


User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = LeadModel
        fields = '__all__'



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username':UsernameField}