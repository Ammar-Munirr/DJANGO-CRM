from django.urls import path
from . import views

app_name = 'leads'
urlpatterns = [
    path('list/',views.LeadList.as_view(),name='lead-list'),
    path('<int:pk>/detail/',views.LeadDetailView.as_view(),name='lead-detail'),
    path('create-lead/',views.LeadCreateView.as_view(),name='lead-create')
]
