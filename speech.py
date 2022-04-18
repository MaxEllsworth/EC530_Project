#!/usr/bin/python3 

import variables
import speech_recognition as sr
import os
from time import sleep
from pydub import AudioSegment
from pydub.silence import split_on_silence 
import uuid
# https://www.geeksforgeeks.org/python-speech-recognition-on-large-audio-files/
# https://en.wikipedia.org/wiki/Harvard_sentences

class audio_file:
    def __init__(self, 
                filesystem_name = "", 
                original_name = "",
                audio_uid = "",
                chunks_indices = (),
                chunk_translations = {},  
                ext = ".wav"):
        self.filesystem_name = audio_uid
        self.original_name = original_name
        self.audio_uid = audio_uid
        self.chunk_indices = [],
        self.chunk_translations = {},
        self.ext = ext
    
    def chunk_path(self,i):
        return variables.chunk_audio_dir + self.audio_uid + "/" + self.audio_uid + "-" + str(i) + self.ext
     



def generate_audio_input_id(audio_input_id = None):
    ''' generates a new audio_input_uid if / until it finds one
        that does not already exist in the originals directory'''
    if (audio_input_id == None) or (type(audio_input_id) != str):
        audio_input_id = uuid.uuid4().hex

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

    return path

def chunkify_using_silence(af):
    
    original_dir = audio_file_locator(af.audio_uid, chunk = False)

    original_path = original_dir + af.filesystem_name + af.ext 

    chunk_path = audio_file_locator(af.audio_uid, chunk = True)#variables.chunk_audio_dir + audio_input_id + "/"

    print("original path is " + original_path)
    audio_input = AudioSegment.from_wav(original_path)

    chunks = split_on_silence(audio_input, 
                    min_silence_len = variables.min_silence_len,
                    silence_thresh = audio_input.dBFS + 2)
                    #variables.silence_threshold)

    i = 0
   
    for chunk in chunks:
        chunk_silent = AudioSegment.silent(duration = 10)
        audio_chunk = chunk_silent + chunk + chunk_silent

        i_chunk_filename = chunk_path + af.audio_uid + "-" + str(i) + af.ext

        audio_chunk.export(i_chunk_filename, bitrate ='192k', format ="wav")
        print("Saved " + i_chunk_filename)
        i += 1 
    af.chunk_indices = i   
   # print(os.listdir(chunk_path))


def transcribe_all_chunks(af):
    r = sr.Recognizer()
    for i in range(0,af.chunk_indices):
       # source = AudioSegment.from_file(file = af.chunk_path(i), format=af.ext)
       source = sr.AudioFile(af.chunk_path(i))
       # with sr.AudioFile(af.chunk_path(i)) as source:
           # try:
        print("translating " + af.chunk_path(i))
        audio_text = r.listen(source)
          #  af.chunk_translations[i] = r.recognize_sphinx(audio_text, language='en')
        af.chunk_translations[i] = r.recognize_google(audio_text, language='en', show_all = True )

            #except:
            #    pass

    

if __name__ == "__main__":
    r = sr.Recognizer()
    audio_f = audio_file(audio_uid =  "f5ce9b47903c4e3099ca71ca6a8e67f1",)

    audio_file_locator(audio_f.audio_uid)
    chunkify_using_silence(audio_f)
    transcribe_all_chunks(audio_f)
    print(audio_f.chunk_translations)