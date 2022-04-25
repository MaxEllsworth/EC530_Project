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
#RUN apt-get install git -y

RUN mongod --fork --logpath /var/log/mongod.log
EXPOSE 27017
workdir /app
RUN apt-get install python3-pip -y
RUN pip3 install flask\
                 pymongo\
                 SpeechRecognition\ 
                 flask-socketio\
                 flask_cors\
                 flatten_json\
                 pydub\
                 pyopenssl\
                 flask-restx\
                 pdoc3
             #    pocketsphinx
copy . .
#ADD bootstrap/ /app/html/bootstrap/
#ADD css/ /app/html/css/
CMD ["python3.8", "./src/speech.py"]
#RUN python3 database.py    