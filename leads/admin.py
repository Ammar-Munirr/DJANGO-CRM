from django.contrib import admin
from .models import LeadModel,Agent,User,UserProfile,Category

@admin.register(LeadModel)
class Leadadmin(admin.ModelAdmin):
    list_display = ['first_name','agent','age']

@admin.register(Agent)
class Agentadmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ['username','email']

admin.site.register(UserProfile)
admin.site.register(Category)
