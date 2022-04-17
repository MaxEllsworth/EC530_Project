FROM ubuntu:latest
workdir /app
RUN apt-get update -y
RUN apt-get install gnupg wget -y
RUN wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add -
RUN wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list
RUN apt-get update -y
RUN apt-get install -y mongodb-org
#RUN service mongodb-server start
RUN systemctl start mongod
RUN systemctl daemon-reload
RUN systemctl status mongod






CMD ["git","clone","git@github.com:twbs/bootstrap.git"]

#FROM mongo:latest
#RUN mongod --fork --logpath /var/log/mongod.log

FROM python:3.8.13-slim-buster
workdir /app
RUN pip3 install flask\
                 pymongo\
                 SpeechRecognition\ 
                 flask-socketio\
                 flask_cors\
                 flatten_json 
copy . . 

CMD ["python3.8", "database.py"]