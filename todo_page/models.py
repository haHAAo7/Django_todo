from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    details = models.TextField(verbose_name="Детали")
    date = models.DateTimeField(default=timezone.now, verbose_name="Дата")

    def __str__(self):
        return self.title
