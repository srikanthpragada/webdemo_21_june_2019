from django.views.generic import TemplateView, ListView
from .models import Employee


class AboutView(TemplateView):
    template_name = "about.html"


class ListEmployeesView(ListView):
    model = Employee
