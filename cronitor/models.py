from django.db import models


class Project(models.Model):
    uid = models.SlugField(db_index=True)
    name = models.TextField()
    auth_token = models.TextField(unique=True, db_index=True)

    def __str__(self):
        return self.name


class Log(models.Model):
    project = models.ForeignKey('Project')
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} at {} from {}'.format(self.project, self.created_at, self.ip_address)
