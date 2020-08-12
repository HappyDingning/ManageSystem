from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.userLogin),
    path('logout/', views.userLogout),
    path('info/', views.userInfo),
    path('customQuery/', views.customQuery),
    path('createStudent/', views.createStudent),
]
