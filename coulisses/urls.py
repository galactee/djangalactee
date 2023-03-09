from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "bonjour/",
        login_required(TemplateView.as_view(template_name="coulisses/bonjour.html")),
    ),
    path("compte/", include("django.contrib.auth.urls")),
    path("check/", TemplateView.as_view(template_name="coulisses/check.html")),
]

"""
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
"""
