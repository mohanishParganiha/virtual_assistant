import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from urllib.parse import quote
import pyowm
from pyowm.utils import timestamps
from datetime import datetime

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
        Weather = current_weather.weather_at_place('Banbarad,India')
        Weather = Weather.weather
        detailed_status = Weather.detailed_status
        temp = Weather.temperature('celsius')['feels_like']
        humidity = Weather.humidity
        return ['current_weather',detailed_status,temp,humidity]

    elif "tomorrows_weather" in query:
        forcast = current_weather.forecast_at_place('Banbarad,India','3h')
        will_rain = forcast.will_be_rainy_at(tomorrow)
        will_sunny = forcast.will_be_clear_at(tomorrow)
        will_cloudy = forcast.will_be_cloudy_at(tomorrow)
        will_stormy = forcast.will_be_stormy_at(tomorrow)
        forecast_weather = []
        new_date = datetime(current_date.year,current_date.month,current_date.day+1)
        new_date = new_date.date()
        for weather in forcast.forecast:
            if str(new_date) in weather.reference_time('iso'):
                forecast_weather.append(
                'reference_time:'+weather.reference_time('iso')+
                ',status:'+weather.status+',detailed_status:'+
                weather.detailed_status+',')
        data_dict = {}
        time_list = []
        status_list = []
        for item in forecast_weather:
            parts = item.split(',')
            for part in parts:
                if 'reference_time' in part:
                    date,time_stamp = part.split(' ')
                    time = time_stamp.split('+')
                    time_list.append(time[0])
                if 'detailed_status' in part:
                    value = part.split(':')
                    status_list.append(value[1])

        for i in range(len(time_list)):
            data_dict[time_list[i]]=status_list[i]
        return ['tomorrows_weather',will_sunny,will_cloudy,will_rain,will_stormy,data_dict]
    
    elif "forecast_weather" in query:
        forcast = current_weather.forecast_at_place('Banbarad,India','3h')
        query = query.replace("forecast_weather ",'')
        weeks = {'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6}
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
        forecast_weather = []
        if given_day in left_days:
            new_date = datetime(current_date.year,current_date.month,current_date.day+given_day+1)
            new_date = new_date.date()
            for weather in forcast.forcast:
                if str(new_date) in weather.reference_time('iso'):
                    forecast_weather.append(
                    'reference_time:'+weather.reference_time('iso')+
                    ',status:'+weather.status+',detailed_status:'+
                    weather.detailed_status+',')
 
        return ['forecast_weather',forecast_weather]
