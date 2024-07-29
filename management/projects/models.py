from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class BaseMixin(models.Model):
    """
    Base mixin class for models.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update date")

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True


class Project(BaseMixin):
    name = models.CharField(verbose_name="Project name", max_length=255, editable=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author_project",
        verbose_name="Author of the project",
    )
    contributor = models.ManyToManyField(
        User,
        related_name="contributor_project",
        verbose_name="Contributors of the project",
    )

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})


class Task(BaseMixin):

    class Condition(models.TextChoices):
        """
        Enum class for selecting a condition.
        """

        todo = "To do"
        in_progress = "In progress"
        done = "Done"
        hot_fix = "Hot fix"

    name = models.CharField(max_length=255, editable=True, verbose_name="Task name")
    condition = models.CharField(choices=Condition.choices, default=Condition.todo, verbose_name="Task condition")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author_task",
        verbose_name="Author of the task",
    )
    contributor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="contributor_task",
        verbose_name="Contributor of task",
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="project_task",
        verbose_name="Task of project",
    )

    def get_absolute_url(self):
        return reverse("task-detail", kwargs={"pk": self.pk})
