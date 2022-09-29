#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz
@author: Bashir AmirKano 
"""
from fabric.api import local, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ["3.235.176.169", "3.227.240.66"]


def do_pack():
    """
    Targging project directory into a packages as .tgz
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None
