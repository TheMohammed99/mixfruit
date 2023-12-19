from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .sidebar import sidebar_data
from .page_title import page_title_data


# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/pages/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Dashboard"
        context["app_name"] = settings.APP_NAME
        context["sidebar_data"] = sidebar_data(active_id=1)
        context["page_title_data"] = page_title_data(name='Dashboard', path_sequence=['Home', 'Dashboard'])
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/pages/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Dashboard"
        context["app_name"] = settings.APP_NAME
        context["sidebar_data"] = sidebar_data(active_id=9)
        context["page_title_data"] = page_title_data(name='Profile', path_sequence=['Home', 'User', 'Profile'])
        return context


class NotFoundView(TemplateView):
    template_name = "dashboard/pages/404.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Dashboard"
        context["app_name"] = settings.APP_NAME
        return context


    @classmethod
    def get_rendered_view(cls):
        as_view_fn = cls.as_view()

        def view_fn(request):
            response = as_view_fn(request)
            response.render()
            return response

        return view_fn