from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/dept/', views.dept_dashboard, name='dept_dashboard'),
    path('dashboard/scheduler/', views.scheduler_dashboard, name='scheduler_dashboard'),
]