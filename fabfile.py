from fabric.api import *
from fabric.contrib.files import *

env.use_ssh_config = True


def test():
    run('uname -a')


def production():
    env.hosts = ['cronitor.bibhas.in']
    env.project_path = '/var/www/cronitor/project/'
    env.venv_path = '/var/www/cronitor/venv/'
    env.git_branch = 'master'


def git_pull(branch):
    with cd(env.project_path):
        sudo('git pull origin {}'.format(branch), user='bibhas')


def pip_install_packages():
    with cd(env.project_path):
        with prefix('source {venv_path}bin/activate'.format(venv_path=env.venv_path)):
            sudo('pip install -r requirements.txt', user='bibhas')


def migrate_all():
    with cd(env.project_path):
        with prefix('source {venv_path}bin/activate'.format(venv_path=env.venv_path)):
            run('python manage.py migrate')


def supervisor_reload():
    sudo('supervisorctl restart cronitor')
    sudo('service nginx restart')


def collectstatic():
    with cd(env.project_path):
        with prefix('source {venv_path}bin/activate'.format(venv_path=env.venv_path)):
            sudo('python manage.py collectstatic --noinput', user='bibhas')


def deploy():
    git_pull(env.git_branch)
    pip_install_packages()
    migrate_all()
    collectstatic()
    supervisor_reload()
