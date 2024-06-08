#!/usr/bin/env python
# coding: utf-8

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from tools.ip_tool import ip_info_tool
from tools.weather_tool import weather_info_tool
from tools.sql_tool import sql_tool
from tools.math_tool import math_tool


# Load environment variables
load_dotenv()

# load fastapi
app = FastAPI()

# instantiate llm
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5)

# define tools
tools = [weather_info_tool,ip_info_tool,sql_tool,math_tool]
agent = initialize_agent(tools, llm, agent='zero-shot-react-description', verbose=True)


# Invoke the agent to fetch weather information for London
@app.get('/question')
def prompt(question: str):
    result = agent.invoke(question)
    return {'output':result}

# prompt('How many suppliers does northwind store have?')
if __name__ == '__main__':
    uvicorn.run(app, host ='127.0.0.1', port= 8000)
    
    
    
