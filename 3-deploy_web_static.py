#!/usr/bin/python3
"""Distributes archive to yo web servers, using do_deploy"""
from fabric.api import *
import os.path
env.hosts = ['34.228.186.149', '34.73.35.13']

def deploy():
    """supposed to pack & deploy, probably won't"""
    pckg = do_pack()
    if pckg is None:
        return False
    return do_deploy(pckg)


def do_deploy(archive_path):
    """Returns False if file at archive_path doesn't exist.
    Uploads archive to /tmp/ directory of web server.
    Uncompresses archive to the folder /data/web_static/releases/<archfile>
    Deletes archive from web server, deletes symbolic link
    /data/web_static/current from web server.
    Creates new symbolic link, linked to new version of code
    Returns True if all is done right, otherwise False"""
    if os.path.isfile(archive_path) is False:
        return False
    path = "/data/web_static/releases/"
    cur = "/data/web_static/current"
    file = archive_path.split('/')[-1]
    name = file.split(".")[0]
    try:
        put(archive_path, "/tmp/")
        run("rm -rf {}{}".format(path, name))
        run("mkdir -p {}{}/".format(path, name))
        run("tar -xzf /tmp/{} -C {}{}/".format(file, path, name))
        run("rm /tmp/{}".format(file))
        run("mv {}{}/web_static/* "
            "{}{}/".format(path, name, path, name))
        run("rm -rf {}{}/web_static".format(path, name))
        run("rm -rf {}".format(cur))
        run("ln -s {}{}/ {}".format(path, name, cur))
        return True
    except:
        return False


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
