FROM mongo:latest 
workdir /app
RUN apt-get update -y
RUN apt-get install gnupg wget -y
RUN wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add -
RUN wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list
RUN apt-get update -y
RUN apt-get install -y mongodb-org
RUN apt-get install ffmpeg -y 
RUN apt-get install net-tools -y
RUN netstat -tulpn
RUN apt-get install git -y
#RUN apt-get install python3-dev -y
#RUN apt-get install pulseaudio -y
#RUN apt-get install swig -y
#RUN mkdir /data/
#RUN mkdir /data/db/
#RUN mkdir /data/db/log
#RUN mongod --dbpath /data/db  --fork --config /etc/mongod.conf  #--fork --logpath /data/db/log
#RUN service mongodb start #mongod --help#service mongodb-server start
#RUN systemctl start mongod
#RUN systemctl daemon-reload
#RUN systemctl status mongod


#FROM mongo:latest
RUN mongod --fork --logpath /var/log/mongod.log
EXPOSE 27017
#FROM python:3.8.13-slim-buster
workdir /app
RUN apt-get install python3-pip -y
#ADD requirements.txt ./
RUN pip3 install flask\
                 pymongo\
                 SpeechRecognition\ 
                 flask-socketio\
                 flask_cors\
                 flatten_json\
                 pydub\
                 pyopenssl\
                 flask-restx
             #    pocketsphinx
copy . .
ADD bootstrap/ /app/html/bootstrap/
ADD css/ /app/html/css/
CMD ["python3.8", "./src/chat.py"]
#RUN python3 database.py    