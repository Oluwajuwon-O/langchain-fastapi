from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from dotenv import load_dotenv
import os
import requests
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool

load_dotenv()
weather_api_key = os.environ['OPENWEATHER_API_KEY']

class WeatherInfo(BaseModel):
    city: str = Field(description= "city")
    
def fetch_weather_info(city:str) -> str:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return response

weather_info_tool = StructuredTool.from_function(func=fetch_weather_info,
                                                name= "Use this tool to fetch weather information about the city supplied",
                                                description= "Fetch weather information about the city from OpenWeather API/url)",
                                                args_schema= WeatherInfo,
                                                return_direct= True)
# llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)
# tools = [weather_info_tool]
# agent = initialize_agent(tools, llm, agent='zero-shot-react-description', verbose=True)

# result = agent.invoke('How is the weather in Lagos?')  
# print(result)