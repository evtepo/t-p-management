from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from projects.models import Project, Task


class AdminSettingsMixin(admin.ModelAdmin):
    show_full_result_count = False
    list_per_page = 20

    class Meta:
        abstract = True


@admin.register(Task)
class TaskAdmin(AdminSettingsMixin):
    list_display = (
        "name",
        "condition",
        "author",
        "contributor",
        "project",
        "created_at",
        "updated_at",
    )
    list_filter = ("condition", "contributor", "project")

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).select_related("author", "contributor", "project")


@admin.register(Project)
class ProjectAdmin(AdminSettingsMixin):
    list_display = ("name", "author", "contributors", "created_at", "updated_at")
    list_filter = ("author",)

    def contributors(self, obj):
        return ", ".join(contributor.username for contributor in obj.contributor.all())
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).select_related("author").prefetch_related("contributor")

    contributors.short_description = "Contributors"
