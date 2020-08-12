"""
Definition of urls for BigdataVisualization.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authtoken import views
from studentUser.views import login

urlpatterns = [
    path('', include('studentUser.urls')),
    path('manage/', include('studentUser.urls')),
    path('admin/', admin.site.urls),
]
