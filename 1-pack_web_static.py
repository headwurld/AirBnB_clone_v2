#!/usr/bin/python3
""" fabric script generates a .tgz archive from the contents
of web_static folder of AirBnB clone repo, using the do_pack function
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """.tgz archive generates from web_static folder"""
    try:
        local('mkdir -p versions')
        now = datetime.now()
        name = "versions/web_static_" + now.strftime("%Y%m%d%H%M%S") + '.tgz'
        local('tar -czvf ' + name + ' web_static')
        return name
    except Exception as e:
        return None
