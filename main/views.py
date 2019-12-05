from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_safe

from main import forms


@require_safe
def index(request):
    return render(request, "main/index.html")


class SignUp(generic.CreateView):
    form_class = forms.MartianUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
