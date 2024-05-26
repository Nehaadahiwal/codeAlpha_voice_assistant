
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os


try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(audio):
