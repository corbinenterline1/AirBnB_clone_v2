#!/usr/bin/python3
"""Generated .gtz archive from contents of web_static."""
from datetime import datetime
from fabric.api import *


def do_pack():
    """Adds all files in web_static to final archive
    All archives stored in folder versions
    Name of archive: web_static_<year><month><day><hour><minute>
    function must return archive path if it's been correctly generated
    Otherwise, return None"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    try:
        file = local('tar -czvf versions/web_static_{}.tgz web_static'
                     .format(time))
        return file
    except BaseException:
        return None
