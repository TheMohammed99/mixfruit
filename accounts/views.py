from django.conf import settings
from .forms import MySignupForm
from allauth.account.views import LoginView, SignupView, LogoutView



# Create your views here.
class MyLoginView(LoginView):
    template_name = 'accounts/pages/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Signin!"
        context["app_name"] = settings.APP_NAME
        return context


class MySignupView(SignupView):
    template_name = 'accounts/pages/signup.html'
    form_class = MySignupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Signup!"
        context["app_name"] = settings.APP_NAME
        return context


class MyLogoutView(LogoutView):
    template_name = 'accounts/pages/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Logout!"
        context["app_name"] = settings.APP_NAME
        return context

