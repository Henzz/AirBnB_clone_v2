#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web
servers using the deploy function
"""

from fabric import task
from fabric.operations import local
from datetime import datetime
import os

# Replace with your web server IP addresses
env.hosts = ['<IP web-01>', '<IP web-02>']


@task
def do_pack(c):
    """
    Generates a .tgz archive from the contents of the web_static folder

    Args:
        c: Fabric connection object
    """
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(now)
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        print('An error occurred: {}'.format(str(e)))
        return None


@task
def do_deploy(c, archive_path):
    """
    Distributes an archive to web servers

    Args:
        c: Fabric connection object
        archive_path (str): Path to the archive file

    Returns:
        bool: True if successful, False otherwise
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Get the archive filename without extension
        archive_filename = os.path.basename(archive_path)
        archive_name = os.path.splitext(archive_filename)[0]

        # Upload the archive to /tmp/ directory on the web server
        c.put(archive_path, '/tmp/')

        # Create the target directory on the web server
        c.run('mkdir -p /data/web_static/releases/{}/'.format(archive_name))

        # Extract the contents of the archive to the target directory
        c.run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
              .format(archive_filename, archive_name))

        # Delete the archive from the web server
        c.run('rm /tmp/{}'.format(archive_filename))

        # Move the extracted contents to the parent directory
        c.run('mv /data/web_static/releases/{}/web_static/* /data/web_static/\
                releases/{}/'.format(archive_name, archive_name))

        # Remove the empty web_static directory
        c.run('rm -rf /data/web_static/releases/{}/web_static'
              .format(archive_name))

        # Delete the symbolic link /data/web_static/current
        c.run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the new version of the code
        c.run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
              .format(archive_name))

        return True
    except Exception as e:
        print('An error occurred: {}'.format(str(e)))
        return False


@task
def deploy(c):
    """
    Creates and distributes an archive to web servers

    Args:
        c: Fabric connection object

    Returns:
        bool: True if successful, False otherwise
    """
    archive_path = do_pack(c)
    if not archive_path:
        return False

    return do_deploy(c, archive_path)
