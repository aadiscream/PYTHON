import time
from win32com.client import Dispatch
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
time = int(timestamp)
voice=Dispatch("Sapi.SpVoice")
if(time>=0 and time <12):
    voice.speak("aag aag aag ")
elif(time>=12 and time<18):
    voice.speak("GOOD AFTERNOON")
elif(time>=18 and time<=24):
    voice.speak("GOOD EVENING")
else:
    voice.speak("invalid input")
    