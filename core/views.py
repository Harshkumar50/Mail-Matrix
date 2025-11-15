from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm, ComposeForm
from .models import Mail


def login_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "Welcome back!")
        return redirect("dashboard")
    return render(request, "login.html", {"form": form})


def register_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = User.objects.create_user(
            username=form.cleaned_data["username"],
            email=form.cleaned_data.get("email"),
            password=form.cleaned_data["password"],
        )
        messages.success(request, "Account created. Please log in.")
        return redirect("login")
    return render(request, "register.html", {"form": form})


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")


@login_required
def dashboard_view(request: HttpRequest) -> HttpResponse:
    inbox_count = Mail.objects.filter(receiver=request.user, is_read=False).count()
    sent_count = Mail.objects.filter(sender=request.user).count()
    return render(request, "dashboard.html", {"inbox_count": inbox_count, "sent_count": sent_count})


@login_required
def inbox_view(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q", "").strip()
    mails = Mail.objects.filter(receiver=request.user)
    if query:
        mails = mails.filter(Q(subject__icontains=query) | Q(sender__username__icontains=query))
    return render(request, "inbox.html", {"mails": mails, "query": query})


@login_required
def sent_view(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q", "").strip()
    mails = Mail.objects.filter(sender=request.user)
    if query:
        mails = mails.filter(Q(subject__icontains=query) | Q(receiver__username__icontains=query))
    return render(request, "sent.html", {"mails": mails, "query": query})


@login_required
def compose_view(request: HttpRequest) -> HttpResponse:
    form = ComposeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        receiver = form.cleaned_data["to"]
        mail = Mail.objects.create(
            sender=request.user,
            receiver=receiver,
            subject=form.cleaned_data["subject"],
            body=form.cleaned_data["body"],
        )
        messages.success(request, "Mail sent successfully.")
        return redirect("sent")
    return render(request, "compose.html", {"form": form})


@login_required
def delete_mail_view(request: HttpRequest, id: int) -> HttpResponse:
    mail = get_object_or_404(Mail, id=id)
    if mail.sender != request.user and mail.receiver != request.user:
        raise Http404("Mail not found.")
    mail.delete()
    messages.info(request, "Mail deleted.")
    next_url = request.GET.get("next") or "dashboard"
    return redirect(next_url)




