from django.urls import path
from .views import DashboardView, ProfileView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile')
]
