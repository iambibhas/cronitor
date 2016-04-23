from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from cronitor.models import Project, Log


class CreateLogView(View):
    model = Log

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uid', '')
        auth_token = self.request.GET.get('auth', '')

        try:
            project = Project.objects.get(
                uid=uid, auth_token=auth_token
            )

            print(request.META.get('REMOTE_ADDR', ''))
            Log.objects.create(
                project=project,
                ip_address=request.META.get('HTTP_X_REAL_IP', '')
            )
            return HttpResponse('OK')
        except Exception as e:
            return HttpResponse('NOTOK: {}'.format(e))


class ProjectDetailsView(DetailView):
    model = Project
    template_name = 'single.html'
    context_object_name = 'project'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        uid = self.kwargs.get('uid')

        project = Project.objects.get(uid=uid)
        return project
