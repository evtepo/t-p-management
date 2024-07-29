from django.contrib.auth.decorators import login_required
from django.urls import path

from projects.views import ProjectCreate, ProjectDetail, ProjectsView


urlpatterns = [
    path("", login_required(ProjectsView.as_view()), name="projects"),
    path("create/", login_required(ProjectCreate.as_view()), name="create"),
    path("project-detail/<pk>", login_required(ProjectDetail.as_view()), name="project-detail"),
]
