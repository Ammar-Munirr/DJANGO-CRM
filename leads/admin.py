from django.contrib import admin
from .models import LeadModel,Agent,User

@admin.register(LeadModel)
class Leadadmin(admin.ModelAdmin):
    list_display = ['first_name','agent','age']

@admin.register(Agent)
class Agentadmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ['username','email']