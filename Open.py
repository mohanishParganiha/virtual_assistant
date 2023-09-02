import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from urllib.parse import quote


def openExe(query):
    query=str(query).lower()

    if "visit" in query or "search" in query:
        nameOfWeb = query.replace("visit ","")
        nameOfWeb = quote(nameOfWeb,safe='')
        url = f"https://www.{nameOfWeb}.com"
        webbrowser.open(url=url)
        return True

    elif "open" in query:
        nameOfApp = query.replace("open","")
        pyautogui.press("win")
        sleep(1)
        keyboard.write(nameOfApp)
        keyboard.press("enter")
        sleep(0.5)
        return True
    
    elif "start" in query:
        nameOfApp = query.replace("open","")
        pyautogui.press("win")
        sleep(1)
        keyboard.write(nameOfApp)
        keyboard.press("enter")
        sleep(0.5)
        return True
    
    elif "email" in query:
        print("email")
        return True

    elif "whatsapp" in query:
        print("whatsapp")
        return True
    