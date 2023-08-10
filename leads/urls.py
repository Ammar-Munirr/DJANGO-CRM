from django.urls import path
from . import views

app_name = 'leads'
urlpatterns = [
    path('list/',views.LeadList.as_view(),name='lead-list')
]
