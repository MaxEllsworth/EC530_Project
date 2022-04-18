#!/usr/bin/bash

#docker-compose up &
# docker system prune -a
docker build -t ec530_docker_image . # --no-cache
docker run  ec530_docker_image #-p 172.17.0.1:27017:27017 ec530_docker_image 
#docker run -d -v ~/Code/EC530/EC530_Project:/app ec530_docker_image

#-p 5000:5000

# docker rmi $(docker images -f "dangling=true" -q)

