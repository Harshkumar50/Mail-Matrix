from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("compose/", views.compose_view, name="compose"),
    path("inbox/", views.inbox_view, name="inbox"),
    path("sent/", views.sent_view, name="sent"),
    path("delete/<int:id>/", views.delete_mail_view, name="delete_mail"),
    path("logout/", views.logout_view, name="logout"),
]




