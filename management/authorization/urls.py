from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.urls import path

from authorization.views import NewPassView, ProfileView, RegistrationView


urlpatterns = [
    path("login/", views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", login_required(views.LogoutView.as_view()), name="logout"),
    path("profile/", login_required(ProfileView.as_view()), name="profile"),
    path("change_password/", login_required(NewPassView.as_view()), name="change_password"),
    path("signup/", RegistrationView.as_view(), name="signup"),
]
