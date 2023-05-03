#!/usr/bin/python3
from fabric.api import local
import os
from datetime import datetime
# Compress before sending

def do_pack():
    # Creating the archive name
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    archive_name = "web_static_" + timestamp + ".tgz"

    # Creating the folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Creating the archive
    archive = local("tar -cvzf versions/{} web_static".format(archive_name))

    # Returning the archive path if the archive is correctly generated,
    # otherwise it should return None
    if archive.failed:
        return None

    return os.path.join("versions", archive)
