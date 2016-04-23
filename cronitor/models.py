from django.db import models
from django.utils import timezone
import datetime


class Project(models.Model):
    uid = models.SlugField(db_index=True)
    name = models.TextField()
    auth_token = models.TextField(unique=True, db_index=True)
    interval = models.IntegerField("Interval in minutes", default=1)

    def __str__(self):
        return self.name


class LogManager(models.Manager):
    def from_today(self):
        queryset = super(LogManager, self).get_queryset()
        return queryset.filter(created_at__gte=datetime.date.today())


class Log(models.Model):
    project = models.ForeignKey('Project')
    created_at = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(default='127.0.0.1')
    is_up = models.BooleanField(default=True)
    message = models.TextField(blank=True, null=True)

    objects = LogManager()

    def __str__(self):
        return '{} at {} from {}'.format(self.project, self.created_at, self.ip_address)

    class Meta:
        ordering = ["-created_at"]
