#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder
"""

from datetime import datetime
from fabric import task
from fabric.operations import local


@task
def do_pack(c):
    """
    Generates a .tgz archive from the contents of the web_static folder

    Args:
        c: Fabric connection object

    Returns:
        str: Archive path if successful, None otherwise
    """

    # Create the versions folder if it doesn't exist
    c.run('mkdir -p versions')

    # Create the archive name using the current timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f'web_static_{timestamp}.tgz'

    # Create the .tgz archive
    result = c.local(f'tar -czvf versions/{archive_name} web_static')

    if result.failed:
        return None
    else:
        return f'versions/{archive_name}'
