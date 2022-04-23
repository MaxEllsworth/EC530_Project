# Installation

Docker is required to run this application in a container (this is recommended). Docker version 20.10.7 was used when originally writing the code. Otherwise, python3 will suffice.  

Before running `docker.sh`, change directory into the `mongo-docker` directory and run `docker-compose up`. This will get the `mongodb` database up and running. 

This project is Dockerized in `Dockerfile`. It is recommended to run it using ./docker.sh, however the line in the `Dockerfile` with `CMD ["python3.8", "./src/api.py"]` will need to be updated in the event that you want to run an alternative application. 


All dependecies are included in the `Dockerfile`, however they can be broken down into the following two categories: ubuntu dependencies, and python3 dependencies:
| Ubuntu | Python3 | 
| ------ | ------- | 
| ffmpeg | flask-restx       |
| gnupg  | flask-socketio    |
| mongodb-org | flask_cors   |
|        | flatten_json      |
|        | pdoc3             |
|        | pydub             |
|        | pymongo           |
|        | pyopenssl         |
|        | SpeechRecognition |  








# Overview

| Modules | Description |
| --------------- | ------------------------------------------------------------------------------ | 
| **[api.py](#API)** | Responsible for pulling together all the separate modules into one RESTful API | 
| **[chat.py](#Chat-Module)** | An in-browser chat application that uses Flask-SocketIO as its backend | 
| **[database.py](#Database)** |  A mongodb wrapper for any device or user action performed via the API | 
| **[devices.py](#Device-Code)** | Loads devices from json templates and instantiates them as objects  |  
| **[speech-queue.py](#Speech-Queue)** | (Experimental) Runs speech to text using multiprocessed queues | 
| **[speech.py](#Speech-To-Text)** |  Class function definitions for splitting, transcribing audio  | 
| **[template.py](#Template-Processor)** | JSON processor for loading user (patient, doctor, etc) profiles | 
| **[tests.py](#Tests)** | Unittest testing | 
| **[users.py](#User-Code)** |  Loads user profiles, instantiates them as objects, updates traits | 
| **[variables.py](#Variable-Definitions)**|  A central location for all of project's static variables |



### API
I elected to create a minimal Flask API  
### Chat Module

### Database

### Device Code

### Speech Queue

### Speech To Text

### Template Processor

### Tests 

### User Code 

### Variable Definitions 

### main.py and web_app.py