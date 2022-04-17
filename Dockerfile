FROM ubuntu:latest
workdir /app
CMD ["git","clone","git@github.com:twbs/bootstrap.git"]

FROM mongo:latest
RUN mongod --fork --logpath /var/log/mongod.log

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