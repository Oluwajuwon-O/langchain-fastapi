#!/usr/bin/env python
# coding: utf-8


from dotenv import load_dotenv
import os
import requests
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool

load_dotenv()

class WeatherInfo(BaseModel):
    city: str = Field(description= "city")
    
def fetch_weather_info(city:str) -> str:
    weather_api_key = os.environ['OPENWEATHER_API_KEY']
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'error fetching weather info.'}

weather_info_tool = StructuredTool.from_function(func=fetch_weather_info,
                                                name= "fetch weather information",
                                                description= "Fetch weather information about the city from OpenWeather API/url)",
                                                args_schema= WeatherInfo,
                                                return_direct= True)

