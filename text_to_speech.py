from picarx import Picarx
from time import sleep
from robot_hat import TTS

tts = TTS()
tts.lang("en-US")
tts.say("hi, I am a robot")
while True:
    text = input("Enter text to speak: ")
    tts.say(text)