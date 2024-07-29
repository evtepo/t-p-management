from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("profile/", login_required(TemplateView.as_view(template_name="profile.html")), name="profile"),
    path("auth/", include("authorization.urls")),
    path("projects/", include("projects.urls")),
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
