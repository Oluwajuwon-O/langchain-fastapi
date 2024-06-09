'''
Weather tool to fetch weather current weather information about given city from openweathermap.org. 
Authentication required.'''

# import necessary libraries
from dotenv import load_dotenv
import os
import requests
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool

# load environment variable
load_dotenv()

# load API key from environment variables
weather_api_key = os.environ['OPENWEATHER_API_KEY']

# Define the schema for the weather information request
class WeatherInfo(BaseModel):
    city: str = Field(description= "city")

# Function to fetch weather information    
def fetch_weather_info(city:str) -> str:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return response

# Define the weather information tool using StructuredTool
weather_info_tool = StructuredTool.from_function(func=fetch_weather_info,
                                                name= "Use this tool to fetch weather information about the city supplied",
                                                description= "Fetch weather information about the city from OpenWeather API/url)",
                                                args_schema= WeatherInfo,
                                                return_direct= True)