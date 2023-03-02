"""
- Проверка сборки проекта
- Создание папок

Virtualization in general
    Virtual machines
    Containerization
Docker
    Intro
    Work with existing images
    Creating own images
    Work with containers
Docker-compose

Useful links:
Github
https://www.virtualbox.org/    VirtualBox VM
https://www.osboxes.org/virtualbox-images/    OS images for VirtualBox
https://docs.docker.com/get-started/overview/
https://hub.docker.com/
https://docs.python.org/3/library/http.server.html    HTTP servers
https://docs.docker.com/engine/reference/commandline/docker/    The base command for the Docker CLI
https://docs.docker.com/engine/reference/builder/    Dockerfile reference
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04    Docker Compose setup
https://docs.python.org/3/howto/logging.html    Logging HOWTO
Created server image
https://hub.docker.com/repository/docker/alexlitvino/server02132023/general
docker pull alexlitvino/server02132023

"""

import os
os.system('docker images -q')