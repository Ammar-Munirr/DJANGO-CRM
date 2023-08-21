from django.urls import path
from . import views

app_name = 'leads'
urlpatterns = [
    path('',views.LeadList.as_view(),name='lead-list'),
    path('<int:pk>/detail/',views.LeadDetailView.as_view(),name='lead-detail'),
    path('create-lead/',views.LeadCreateView.as_view(),name='lead-create'),
    path('<int:pk>/update-lead/',views.LeadUpdateView.as_view(),name='lead-update'),
    path('<int:pk>/lead-delete/',views.LeadDeleteView.as_view(),name='lead-delete'),
    path('<int:pk>/assign-agent/',views.AssignAgentView.as_view(),name='assign-agent'),
    path('categories/',views.CategoryListView.as_view(),name='category-list')
]
