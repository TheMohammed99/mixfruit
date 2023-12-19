from django.urls import path
from .views import MyLoginView, MySignupView, MyLogoutView


urlpatterns = [
    path('login/', MyLoginView.as_view(), name='account_login'),
    path('signup/', MySignupView.as_view(), name='account_signup'),
    path('logout/', MyLogoutView.as_view(), name='account_logout'),
]
