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

    def get_powercut_duration(self, date):
        offline_logs = self.log_set.filter(created_at__date=date, is_up=False)
        total_offline_seconds = 0

        for offline_log in offline_logs:
            previous_log = offline_log.get_previous_by_created_at()
            next_log = offline_log.get_next_by_created_at()
            difference_seconds = next_log.created_at - previous_log.created_at
            total_offline_seconds += difference_seconds.second
        return total_offline_seconds

    def get_history(self):
        dates = set()
        for log in self.log_set.all():
            dates.add(log.created_at.date())

        powercut_history = {
            '2016-04-26': 15
        }
        for date in dates:
            powercut_history[date.isoformat()] = self.get_powercut_duration(date)
        return powercut_history


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
