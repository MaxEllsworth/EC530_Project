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
                audio_uid = None,
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
     



    def generate_audio_input_id(self):#, audio_uid = None):
        ''' generates a new audio_input_uid if / until it finds one
            that does not already exist in the originals directory'''
        if (self.audio_uid == None) or (type(self.audio_uid) != str):
            self.audio_uid = uuid.uuid4().hex

        original_audio_path = variables.original_audio_dir + self.audio_uid + "/"
        while os.path.exists(original_audio_path): 
            self.audio_uid = uuid.uuid4().hex
            original_audio_path = variables.original_audio_dir + self.audio_uid + "/"

        return self.audio_uid
        

    def audio_file_locator(self, chunk=False):#,audio_input_id, chunk = False):
        ''' Purpose is to take an ID and determine if and whether an original 
        and chunk directory exists. If none do, then it makes them.'''
            # audio input ID will have to be a uuid

        if chunk:
            root_path = variables.chunk_audio_dir
        if not chunk:
            root_path = variables.original_audio_dir

        path = root_path + self.audio_uid + "/"
    
        if not os.path.isdir(path):
            os.mkdir(root_path)
            os.mkdir(path)

        return path

    def chunkify_using_silence(self):

        original_dir = self.audio_file_locator(chunk = False)

        original_path = original_dir + self.filesystem_name + self.ext 

        chunk_path = self.audio_file_locator(chunk = True)#variables.chunk_audio_dir + audio_input_id + "/"

        print("original path is " + original_path)
        audio_input = AudioSegment.from_wav(original_path)

        chunks = split_on_silence(audio_input, 
                    #    min_silence_len = variables.min_silence_len,
                        silence_thresh = audio_input.dBFS + 1,
                        keep_silence = True)
                        #variables.silence_threshold)

        i = 0
    
        for chunk in chunks:
            i_chunk_filename = chunk_path + self.audio_uid + "-" + str(i) + self.ext
            chunk.export(i_chunk_filename, bitrate = "192k", format="wav")
            i += 1 
        self.chunk_indices = i   


    def transcribe_chunks(self, transcribe_all = False, chunk_index = None):
        min_iter = 0
        max_iter = 0
        if (transcribe_all):
            max_iter = self.chunk_indices
        
        else:
            min_iter = chunk_index
            max_iter = chunk_index + 1:
            

        if 
        for i in range(min_iter,max_iter):
            f = sr.AudioFile(self.chunk_path(i))
            with f as source:            
                r = sr.Recognizer()
                r.adjust_for_ambient_noise(source)  
                audio = r.record(source)
                chunk_text = str(r.recognize_google(audio, language='en', show_all = True )['alternative'][0]['transcript'])
                self.chunk_translations[0][i] = chunk_text




if __name__ == "__main__":
    r = sr.Recognizer()
    audio_f = audio_file(audio_uid =  "f5ce9b47903c4e3099ca71ca6a8e67f1",)

    audio_f.audio_file_locator(audio_f.audio_uid)
    audio_f.chunkify_using_silence()
    print("this code is so messed up")
    audio_f.transcribe_chunks()
    print(audio_f.chunk_translations)
  #  sleep(100000)