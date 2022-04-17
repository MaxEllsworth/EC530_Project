#!/usr/bin/bash

docker build -t ec530_docker_image . #--no-cache
docker run -v ~/Code/EC530/EC530_Project:/app -p 5000:5000  ec530_docker_image