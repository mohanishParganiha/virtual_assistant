import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from urllib.parse import quote
import pyowm
from pyowm.utils import timestamps
from datetime import datetime

location = "Banbarad,India"

open_weather_api_key='14db83cc45d773c50212aa030e74fc1a'
owm = pyowm.OWM(open_weather_api_key)
current_weather = owm.weather_manager()
tomorrow = timestamps.tomorrow()

weekday = datetime.today().weekday()
current_date = datetime.today()


def openExe(query):
    query=str(query).lower()

    if "visit" in query or "search" in query:
        nameOfWeb = query.replace("visit ","")
        nameOfWeb = quote(nameOfWeb,safe='')
        url = f"https://www.{nameOfWeb}.com"
        webbrowser.open(url=url)
        return True

    elif "open" in query or "start" in query:
        nameOfApp = query.replace("open","")
        pyautogui.press("win")
        sleep(1)
        keyboard.write(nameOfApp)
        keyboard.press("enter")
        sleep(0.5)
        return True
    
    
    elif "email" in query:
        return ['email']
    

    elif "whatsapp" in query:
        return ['whatsapp']
    
    elif "current_weather" in query:
        Weather = current_weather.weather_at_place(location)
        Weather = Weather.weather
        detailed_status = Weather.detailed_status
        temp = Weather.temperature('celsius')['feels_like']
        humidity = Weather.humidity
        return ['current_weather'," current weather at ",location," is ",detailed_status," temperature is ",temp," humidity is ",humidity]

    elif "tomorrows_weather" in query:
        forcast = current_weather.forecast_at_place(location,'3h')
        will_rain = forcast.will_be_rainy_at(tomorrow)
        will_sunny = forcast.will_be_clear_at(tomorrow)
        will_cloudy = forcast.will_be_cloudy_at(tomorrow)
        will_stormy = forcast.will_be_stormy_at(tomorrow)
        forecast_weather = []
        new_date = datetime(current_date.year,current_date.month,current_date.day+1,12,0,0)
        for weather in forcast.forecast:
            if str(new_date) in weather.reference_time('iso'):
                forecast_weather.append(
                'reference_time:'+weather.reference_time('iso')+
                ',status:'+weather.status+',detailed_status:'+
                weather.detailed_status+',')
        status = "none"
        for i in forecast_weather:
                status = i.split(',')
                status = status[1]
                status = status.split(":")
                status = status[1]
                break
        return ['tomorrows_weather',will_sunny,will_cloudy,will_rain,will_stormy,status]
    
    elif "forecast_weather" in query:
        forecast = current_weather.forecast_at_place(location,'3h')
        query = query.replace("forecast_weather ",'')
        weeks = {'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6,'mondays':0,'tuesdays':1,'wednesdays':2,'thursdays':3,'fridays':4,'saturdays':5,'sundays':6}
        for keys in weeks.keys():
            if keys in query:
                given_day = weeks[keys]
        left_days = []
        today = datetime.today().weekday()
        days = 0
        while True:
            if days == today and today+1 <= 6:
                left_days.append(days+1)
                today += 1
            elif today == 6:
                today = -1 
                days = -1
                continue
                # left_days_next_week = list(week_days.values())
            if len(left_days) == 5:
                break
            days += 1
        given_date = None
        new = datetime(current_date.year,current_date.month,current_date.day)
        if given_day in left_days:
            while True:
                if new.weekday() == given_day:
                    given_date = new
                    break
                new = datetime(current_date.year,current_date.month,new.day+1)
        else:
            return "give date or day is out of forecast range"
        forecast_weather = []
        given_date = datetime(given_date.year,given_date.month,given_date.day,12,0,0)
        if given_day in left_days:
            for weather in forecast.forecast:
                if str(given_date) in weather.reference_time('iso'):
                    forecast_weather.append(
                    'reference_time:'+weather.reference_time('iso')+
                    ',status:'+weather.status+',detailed_status:'+
                    weather.detailed_status+',')
        status = None
        for i in forecast_weather:
            status = i.split(',')
            status = status[1]
            status = status.split(":")
            status = status[1]
            break

        return ['forecast_weather',str(given_date.date()),status]
