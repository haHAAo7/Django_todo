from django.db import models
from django.utils import timezone
from datetime import timedelta

date_now = timezone.now()
next_week = date_now + timedelta(days=7)


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    details = models.TextField(verbose_name="Детали")
    date = models.DateTimeField(default=date_now, verbose_name="Дата добавления")
    deadline = models.DateTimeField(default=next_week, verbose_name="Дедлайн")

    def __str__(self):
        return self.title
