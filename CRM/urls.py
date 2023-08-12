from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from leads.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/',include('leads.urls',namespace='leads')),
    path('',Home.as_view(),name='home')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)