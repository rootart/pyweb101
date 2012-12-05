from __future__ import with_statement
from fabric.api import run, put, sudo, env, cd, local, prefix
from fabric.context_managers import settings
from fabric.colors import red, green


def prod():
    env.hosts = ['pythonweb-class.org',]
    env.user = 'pyweb'
    env.project_dir = '/home/pyweb/pyweb101/src/'
    env.name = 'pythonweb_class.org'

def run_command(command):
    run(command)

def git(command):
    with cd(env.project_dir):
        run("git %s" % command)

def restart():
    run("sudo supervisorctl restart %s" % env.name)

def django(command):
    with cd(env.project_dir):
        with prefix("source ~/env/bin/activate"):
            run("python manage.py %s" % command)


def deploy():
    git("pull")
    django("migrate")
    django("collectstatic -l --noinput")
    restart()