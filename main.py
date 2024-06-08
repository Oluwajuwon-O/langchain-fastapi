#!/usr/bin/env python
# coding: utf-8


from langchain.agents import initialize_agent
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn


# Load environment variables
load_dotenv()

app = FastAPI()


# tools = [weather_tool, sql_tool]
# agent = initialize_agent(tools, llm, agent='zero-shot-react-description', verbose=True)

    
# Invoke the agent to fetch weather information for London
# @app.get('/question')
# def prompt(question: str):
#     result = agent.invoke(question)
#     return {'output':result}

# prompt('How many suppliers does northwind store have?')
if __name__ == '__main__':
    uvicorn.run(app, host ='127.0.0.1', port= 8000)
    
    
    
