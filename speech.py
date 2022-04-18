#!/usr/bin/python3 

import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence 
# https://www.geeksforgeeks.org/python-speech-recognition-on-large-audio-files/
# https://en.wikipedia.org/wiki/Harvard_sentences

if __name__ == "__main__":
    r = sr.Recognizer()
