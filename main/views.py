from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_http_methods, require_safe

from main import forms, models


@require_safe
def index(request):
    return render(
        request,
        "main/index.html",
        {"pins": models.Pin.objects.filter(user=request.user)},
    )


class SignUp(generic.CreateView):
    form_class = forms.MartianUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@require_http_methods(["GET", "POST"])
@login_required
def hashpin(request):
    if request.method == "POST":
        form = forms.CreateHashPin(request.POST)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.user = request.user
            pin.save()
            messages.success(request, "Pin created")
            return redirect("main:index")
        else:
            print(form.errors)
    else:
        form = forms.CreateHashPin()

    return redirect("main:index")
    # return render(
    #     request,
    #     "main/index.html",
    # )
