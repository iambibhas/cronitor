from django.contrib import admin
from cronitor.models import Project, Log

admin.site.register([Project, Log])
