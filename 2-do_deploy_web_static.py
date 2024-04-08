#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers using the do_deploy function
"""

from fabric import task
from fabric.operations import put, run, sudo
from os.path import exists
from datetime import datetime
import os


env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with your web server IP addresses


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
    if not exists(archive_path):
        return False

    try:
        # Get the archive filename without extension
        archive_filename = os.path.basename(archive_path)
        archive_name = os.path.splitext(archive_filename)[0]

        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Create the target directory on the web server
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_name))

        # Extract the contents of the archive to the target directory
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_filename, archive_name))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Move the extracted contents to the parent directory
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(archive_name, archive_name))

        # Remove the empty web_static directory
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_name))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the new version of the code
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_name))

        return True
    except Exception as e:
        print('An error occurred: {}'.format(str(e)))
        return False
