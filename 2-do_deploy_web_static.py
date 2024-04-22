#!/usr/bin/python3
""" Fabric script distributes an archive to my servers 
    using do_deploy
"""

from fabric.api import env
from fabric.api import put
from fabric.api import sudo
from datetime import datetime
from os import path


env.hosts = ['54.160.65.25', '3.90.80.134']


def do_deploy(archive_path):
    """ Distributes an archive to the web servers
    """
    try:
        if not path.exists(archive_path):
            return False
        put(archive_path, '/tmp/')
        # string slicing
        fold = archive_path[9:-4]
        now = '/data/web_static/current'
        web_folder = '/data/web_static/releases/'
        # sudo command
        sudo('mkdir -p {}{}'.format(web_folder, fold))
        sudo('tar -zxvf /tmp/{0}.tgz -C {1}{0}'.format(fold, web_folder))
        sudo('mv {0}{1}/web_static/* {0}{1}/'.format(web_folder, fold))
        # remove unwanted files
        sudo('rm /tmp/{}.tgz'.format(fold))
        sudo('rm -rf {0}{1}/web_static'.format(web_folder, fold))
        sudo('rm ' + now)
        # Create symbolic link to web_static folder
        sudo('ln -s {}{} {}'.format(web_folder, fold, now))
        return True
    except Exception as e:
        return False
