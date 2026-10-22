from win32com.client import Dispatch
from plyer import notification
import time

voice=Dispatch("Sapi.SpVoice")
while True:
    notification.notify(
        title = "ALERT!",
        message="!!Please Drink water Aditya!!",
        app_icon="D:\\PROGRAMMING\\PYTHON\\png\\water.ico",
        timeout=5
    )
    voice.speak("Pani pee leeee Aditya")
    time.sleep(4)