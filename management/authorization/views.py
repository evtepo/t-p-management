from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView


class NewPassView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "change_pass.html"
    success_url = reverse_lazy("home")


class ProfileView(DetailView):
    model = User
    template_name = "profile.html"

    def get_object(self, queryset = None):
        return self.request.user


class RegistrationView(FormView):
    template_name = "signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        new_user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, new_user)
        return HttpResponseRedirect(self.get_success_url())
    
