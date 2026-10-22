from win32com.client import Dispatch
s=Dispatch("SAPI.SpVoice")
name=["aditya","amit","konal","dinesh", "himanshu"]
for i in name:
    s.speak(f"shoutout to {i}")
