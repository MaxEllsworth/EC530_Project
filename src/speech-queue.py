#!/usr/bin/python3

import multiprocessing
import time
import speech_recognition as sr
from speech import audio_file
 
def queue_transcribe_chunks(msgQueue, af, chunk_index):
    chunk_text = af.transcribe_chunks(transcribe_all = False, chunk_index = chunk_index)
    print("chunk text is " + chunk_text)
    msgQueue.put(str(chunk_text))
    time.sleep(1)
    
# Producer/Writer

def procFunction0(messageQueue):

    for i in range(1,10):

        messageQueue.put("Child1:Message%d"%i)

        time.sleep(1)

 

# Consumer/Reader

def procFunction1(messageQueue):
    while messageQueue.empty() is False:
        print("From reader:%s"%messageQueue.get())
        time.sleep(1)

 

# Producer/Writer

def procFunction2(messageQueue):

    for i in range(1,10):

        messageQueue.put("Child3:Message%d"%i)

        time.sleep(1)

 

if __name__ == "__main__":

 
    r = sr.Recognizer()
    audio_f = audio_file(audio_uid =  "f5ce9b47903c4e3099ca71ca6a8e67f1",)

    audio_f.audio_file_locator(audio_f.audio_uid)
    audio_f.chunkify_using_silence()
    print("this code is so messed up")



    multiprocessing.set_start_method("fork")

   

    messageQueue  = multiprocessing.Queue()

   

    # Create child processes

    childProcess0 = multiprocessing.Process(target=queue_transcribe_chunks, args=(messageQueue,audio_f, 0))

    childProcess1 = multiprocessing.Process(target=procFunction1, args=(messageQueue,))

 #   childProcess2 = multiprocessing.Process(target=procFunction2, args=(messageQueue,))

 

    # Start all the child processes - Writer, Reader, Writer

    childProcess0.start()

    childProcess1.start()

  #  childProcess2.start()

 

    # Wait for child processes to finish

    childProcess0.join()

    childProcess1.join()

 #   childProcess2.join()

    print(audio_f.chunk_translations)
if __name__ != "__main__":
    True
  #  sleep(100000)