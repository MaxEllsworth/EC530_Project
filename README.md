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
I elected to create a minimal Flask API by using Flask blueprints. After writing all of my separate modules, I went back through them and modified them so that individual functions would return Flask responses. I then connected them all to my web application in `api.py` by using Flask blueprints. By instantiating my functions as Flask blueprints, I could have them defined in multiple different files, import them all in `api.py`, and then have them automatically populate as routes in Flask. 

### Chat Module
The chat module uses the following libraries / code written by other people:
- [Flask](https://pypi.org/project/Flask/)
- [Flask-SocketIO](https://pypi.org/project/Flask-SocketIO/)
- [Bootstrap](https://github.com/twbs/bootstrap)
- [Brijesh Bittu's chat `css` code](https://codepen.io/brijeshb42/pen/pprmeO)

I added used both the `chat.css` code and css code native to Bootstrap. I also added Javascript code which would populate the html page with message boxes as they were received / sent. The actual messages were sent using Flask-SocketIO through in-browser SocketIO messages. The way Flask-SocketIO works is that it routinely polls the browser in the background. 

### Database
I elected to use MongoDB (a Docker [`mongod`](https://hub.docker.com/_/mongo) service and the [`pymongo`](https://pypi.org/project/pymongo/) library). I found the PyMongo interface to be far better than that of sqlite3, in which arguments are passed as strings. 

```
mongo_user_wrapper class:
  class variables:
    user_object: 
    client: 
  class functions:
    show:
      '''
      Shows collection for a given user category 
      (doctor, patient, administrator)
      '''
    save:    
      '''
      Saves user object and all class variables in the user object's class. 
      The user class is defined by a meta object (a class that returns a class) 
      in which the class variables are defined by the user template (json). 
      The implication of this is that the user object can have whatever variables 
      it likes, and the database save function will save them regardless. 
      This is done using a flatten_json function which is included in `database.py` 
      and an additional key:value pair of cao:{datetime} is added 
      to this json before it is saved.
      '''
```

### Device Code
The device module is responsible for importing templates (currently json files).   

### Speech Queue
The speech queue is just an implementation of the [speech to text](#Speech-To-Text) module where the transcription function is executed as a target process in a multiprocess queue. The benefit of using mulitiprocess queues is that they are native to Python3 and do not require any extra broker servers to be running in the background. This part of the project is not completely flushed out and still requires a bit of work, however the basic outline is there.  
### Speech To Text
This implementation of speech transcription uses `pydub` for processing (splitting on silence), the `speech_recognition` (`sr`) Python library, and the Google speech API (`r.recognize_google()`) accompanying `sr`. 

In order to perform transcription, the audio file and associated metadata (storage location, uid) are congregated in an `audio_file` object. The `audio_file` class has all the functions required for performing transcription, which include the following:
- Locating the audio file on disk and verifying it exists
- Splitting of the large audio file into smaller chunks using `pydub`
- Generating unique IDs for the audio files and chunks using the Python `uuid` library
- Transcription using Google's API via `speech_recognition`

The test data used is a recording of a [Harvard sentence](https://www.cs.columbia.edu/~hgs/audio/harvard.html). The Harvard sentences are a collection of 72 different blocks of text. Each block has ten sentences / phrases in it. The original purpose of the Harvard sentences was to test VOIP systems. Under `audio/originals/` is a recording of Harvard sentence #57. This is the sample audio used to test the speech recognition module. 

### Template Processor
The template processor takes a template ID (patient, doctor, etc.) as an input, loads the json file, and outputs the contents as a JSON object 
#### Patient Template
``` json
{"identity" : 
    {
    "fname" : "",
    "lname" : "",
    "dob" : "",
    "sex" : "" 
    },

"visitMetrics" : 
    {"visitDate" : "",
    "attendingNurse" : "",
    "attendingDoctor" : "",
    "healthMetrics" : 
        {
            "height" : "",
            "weight" : "",
            "systolic" : "",
            "diastolic" : ""
        }
    }
}
```

#### Doctor Template
```json
{
    "identity" : 
    {
    "fname" : "",
    "lname" : "",
    "dob" : "",
    "sex" : "" 
    },
    "specialties" : 
    {

    },
    "offices" : 
    {

    }
}
```

### Tests 
`unittest` testing
### User Code 
Like the device module but for user roles instead, it is responsible for loading the JSON templates for different users (patient, doctor, administrator) and merging new information passed about those users with the fields defined in the user templates.  

### Variable Definitions 
All static variables, particularly those defining the template locations, MongoDB settings, and Flask configuration options, are defined in one file, `variables.py`. These variables are then imported to the other modules using `import variables`. The advantage of doing it this way is that it is easier to keep track of all the variables that it may be desirable to update along the development process and to make those changes in one place.   
<!--### main.py and web_app.py-->

