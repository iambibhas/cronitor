from django.db import models


class Project(models.Model):
    uid = models.SlugField()
    name = models.TextField()
    auth_token = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Log(models.Model):
    project = models.ForeignKey('Project')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} at {}'.format(self.project, self.created_at)
