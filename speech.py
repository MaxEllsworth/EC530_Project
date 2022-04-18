#!/usr/bin/python3 

import variables
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence 
import uuid
# https://www.geeksforgeeks.org/python-speech-recognition-on-large-audio-files/
# https://en.wikipedia.org/wiki/Harvard_sentences

def generate_audio_input_id(audio_input_id):
    ''' generates a new audio_input_uid if / until it finds one
        that does not already exist in the originals directory'''
    original_audio_path = variables.original_audio_dir + audio_input_id + "/"
    while os.path.exists(original_audio_path): 
        audio_input_id = uuid.uuid4().hex
        original_audio_path = variables.original_audio_dir + audio_input_id + "/"

    return audio_input_id
        

def audio_file_locator(audio_input_id, chunk = False):
    ''' Purpose is to take an ID and determine if and whether an original 
    and chunk directory exists. If none do, then it makes them.'''
        # audio input ID will have to be a uuid
    
    if chunk:
        root_path = variables.chunk_audio_dir
    if not chunk:
        root_path = variables.original_audio_dir

    path = root_path + audio_input_id + "/"
   
    if not os.path.isdir(path):
        os.mkdir(root_path)
        os.mkdir(path)


def chunkify_using_silence(audio_input_id):
    
    audio_input = AudioSegment.from_wav(path)


    try:
        os.mkdir()
    except (FileExistsError):
        pass


def transcribe_chunk():
    True

if __name__ == "__main__":
    r = sr.Recognizer()
    audio_file_locator("test_id_2")