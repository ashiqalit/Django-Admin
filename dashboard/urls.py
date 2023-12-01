from django.urls import path
from dashboard import views

urlpatterns = [
    path ('', views.dash, name = 'dash'),
    path ('login', views.login, name = 'dashboard_login'),
    path ('logout', views.logout, name = 'dashboard_logout'),
    path ('create/', views.create_user, name = 'create_user'),
    path ('read/', views.read_user, name = 'read_user'),
    path ('update/<int:pk>/', views.update_user, name = 'update_user'),
    path ('delete/<int:pk>/', views.delete_user, name = 'delete_user'),
]



