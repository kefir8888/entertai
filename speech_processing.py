# coding=utf-8

import wikipedia
from gtts import gTTS
from multiprocessing import Process
from multiprocessing.queues import Queue
import time
import speech_recognition as sr

"""class Speech_parser(Process):
    def __init__ (self):
        Process.__init__ (self)
        
        self.init_recognition ()

    def set_connection (self, connection):
        self.connection = connection

    def init_recognition (self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone (device_index=0)
    
    def get_audio (self):
        with self.microphone as source:
            print ("listening...")
            self.audio = self.recognizer.listen (source)

            return self.audio

    def recognize (self):
        success = True

        try:
            self.recognized = self.recognizer.recognize_google (self.audio, language = 'ru-RU')
            print ("recognized", self.recognized)

        except:
            print ("cannot recognize")
            success = False
	    self.recognized = 0

        return success, self.recognized
    
    def run (self):
        print ("started listening loop")
        
        while (True):
            time.sleep (0.1)
            
            self.get_audio ()
            
            succ, recognized = self.recognize ()
            
            message = {"success"    : succ,
                       "recognized" : recognized}
            
            self.connection.put (message)"""

class Words_processor:
    def __init__ (self):
        wikipedia.set_lang ("ru")
    
    def get_wiki_content (self, input_data):
        succ = True

        self.content = []

        try:
            print ("input in wikisearch", input_data)
            self.page = wikipedia.page (input_data)
            print (self.page.url)
            print (self.page.title)

            self.content = self.page.content # Content of page.
            self.to_generate = self.content [:100]
            #print ("to generate:", self.to_generate)

        except:
            succ = False

        return succ, self.content

    def generate_mp3 (self, input_text, filename = "1.mp3"):
        #print ("generating:", self.to_generate)
        
        succ = True

        try:
            print ("text generation in progress")
            tts = gTTS (input_text, lang='ru')
        
            new_filename = u"%s" % filename
            tts.save (new_filename)
        
        #tts.save (filename)

        except:
            pass
            #print ("cannot generate file")
            #succ = False

        return succ, filename

class Dialogue_system:
    def __init__ (self):
        pass

    def response_in_dialogue (self, phrase):
        #phrase is a list of words
        

        print ("phrase", phrase)

        commands = []

        if (u"%s" % "сядь" in phrase):
            commands.append ({"type"           : "action",
                              "execution_time" : 0,
                              "contents"       : "/rest",
                              "parameter"      : "1.mp3"})

        elif ("Тань" in phrase):
            commands.append ({"type"           : "action",
                              "execution_time" : 0,
                              "contents"       : "/stand",
                              "parameter"      : "1.mp3"})

        print ("after analyzing", commands)
        
        return commands