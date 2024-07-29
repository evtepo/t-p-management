from typing import Any
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseBadRequest
from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse

from projects.models import Project, Task


class ProjectsView(ListView):
    context_object_name = "projects"
    http_method_names = ["get"]
    template_name = "project.html"

    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        projects = (
            Project.objects.filter(contributor=user)
            .select_related("author")
            .prefetch_related("contributor")
        )

        return projects
    

class ProjectCreate(CreateView):
    model = Project
    fields = ["name"]
    template_name = "create_project.html"

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if not (project_name := request.POST["name"]):
            return HttpResponseBadRequest("Projcet name cannot be empty.")
        
        project = Project(name=project_name, author=request.user)
        project.save()

        return HttpResponseRedirect(reverse("project-detail", kwargs={"pk": project.pk}))


class ProjectDetail(DetailView):
    ...
