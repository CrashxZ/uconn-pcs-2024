from picarx import Picarx
from time import sleep
from robot_hat import TTS

tts = TTS()
tts.lang("en-US")
tts.say("Hello, I am a robot")

text = input("Enter text to speak: ")
tts.say(text)
