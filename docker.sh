#!/usr/bin/bash

docker build -t ec530_docker_image . --no-cache
docker run -d -v ~/Code/EC530/EC530_Project:/app ec530_docker_image
#-p 5000:5000