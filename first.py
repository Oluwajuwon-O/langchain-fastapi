#!/usr/bin/env python
# coding: utf-8


import os
import requests
from langchain_openai import ChatOpenAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
# from langchain.agents import AgentExecutor
from langchain.tools import Tool
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
    if weather_data == 'error':
        return "Unable to fetch weather information at the moment."
    main = weather_data['main']
    weather_desc = weather_data['weather'][0]['description']
    return f"The weather in {city} is {weather_desc} with a temperature of {main['temp']}°C."

# Create a Tool for fetching weather data
weather_tool = Tool(name='fetch_weather_data', description='Gets weather info', func=fetch_weather_info)

@app.get('/')
def index():
    return {'message': 'Welcome'}



@app.post('/result')
def query_db(query:str):
    # Initialize the SQL database
    db = SQLDatabase.from_uri('sqlite:///northwind.db')
    
    # Initialize the language model
    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)
    
    # Create a toolkit with the database and additional tools
    toolkit = SQLDatabaseToolkit(db=db, llm=llm, extra_tools=[weather_tool])
    
    # Create an agent executor with the language model and toolkit
    agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=False)
    
    # Invoke the agent to fetch weather information for London
    result = agent_executor.invoke(query)
    return result


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=8000)



# get_ipython().system('jupyter nbconvert --to script first.ipynb')

