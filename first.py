#!/usr/bin/env python
# coding: utf-8

import os
import requests
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.tools import Tool, QuerySQLDataBaseTool
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

# Load environment variables
load_dotenv()

app = FastAPI()



# WeatherAPI class to interact with OpenWeather API
class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return 'error'

# Initialize the WeatherAPI with the API key from environment variable
weather_api = WeatherAPI(os.environ['OPENWEATHER_API_KEY'])


    
# Function to fetch weather information using WeatherAPI
def fetch_weather_info(city):
    weather_data = weather_api.get_weather(city)
    return weather_data

# Create a Tool for fetching weather data
weather_tool = Tool(name='fetch_weather_data', description='Gets weather info', func=fetch_weather_info)

   
# Initialize the language model
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)

# Initialize the SQL database
db = SQLDatabase.from_uri('sqlite:///northwind.db')
sql_tool = QuerySQLDataBaseTool(db=db, llm= llm)
 

tools = [weather_tool, sql_tool]
agent = initialize_agent(tools, llm, agent='zero-shot-react-description',verbose=True)

    
# Invoke the agent to fetch weather information for London
@app.post('/question')
def prompt(question: str):
    result = agent.invoke(question)
    return {'output':result}

# prompt('How many suppliers does northwind store have?')
if __name__ == '__main__':
    uvicorn.run(app, host ='127.0.0.1', port= 8000)
    
    
    
