from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_http_methods, require_safe

from main import forms, models, tasks


@require_safe
def index(request):
    return render(
        request,
        "main/index.html",
        {
            "pins": models.Pin.objects.filter(user=request.user)
            if request.user.is_authenticated
            else []
        },
    )


@require_safe
def terms(request):
    return render(request, "main/terms.html")


class SignUp(generic.CreateView):
    form_class = forms.MartianUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@require_http_methods(["GET", "POST"])
@login_required
def hashpin(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "GET":
        return redirect("main:index")

    form = forms.CreateHashPinForm(request.POST)
    if form.is_valid():
        pin = form.save(commit=False)
        pin.user = request.user
        pin.save()
        tasks.ipfs_pin_add(pin.ipfs_hash)
        messages.info(request, "INFO: Pin submitted.")
    else:
        for field, errors in form.errors.items():
            messages.error(request, f"ERROR: {field}: {','.join(errors)}")

    return redirect("main:index")


@require_http_methods(["GET", "POST"])
@login_required
def uploadpin(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "GET":
        return redirect("main:index")

    form = forms.UploadHashPinForm(request.POST, request.FILES)
    if form.is_valid():
        ipfs_file = request.FILES["ipfs_file"]
        ipfs_file_path = f"/tmp/{ipfs_file.name}"
        with open(ipfs_file_path, "wb+") as destination:
            for chunk in ipfs_file.chunks():
                destination.write(chunk)
        tasks.ipfs_add(ipfs_file_path)
        messages.info(request, "INFO: IPFS add operation started.")
    else:
        for field, errors in form.errors.items():
            messages.error(request, f"ERROR: {field}: {','.join(errors)}")

    return redirect("main:index")


@require_http_methods(["GET", "POST"])
@login_required
def rm_pin(request, pin_id):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "GET":
        return redirect("main:index")

    form = forms.PinDeletionForm({"id": pin_id})
    if form.is_valid():
        pin = models.Pin.objects.get(id=pin_id)

        # if only user to have set ipfs file, then delete it
        # otherwise, delete only pin
        if models.Pin.objects.filter(ipfs_file=pin.ipfs_file).count() == 1:
            pin.ipfs_file.delete()
            tasks.ipfs_pin_rm(pin.ipfs_file.ipfs_hash)

        pin.delete()
        messages.info(request, "INFO: Pin delete operation started.")
    else:
        for field, errors in form.errors.items():
            messages.error(request, f"ERROR: {field}: {','.join(errors)}")

    return redirect("main:index")
