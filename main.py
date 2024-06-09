# import modules and libraries
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

# Initialize FastAPI application
app = FastAPI()

# Instantiate the language model 
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5)

# Define the tools to be used by the agent
tools = [weather_info_tool, ip_info_tool, sql_tool, math_tool]

# Initialize the agent with the defined tools and the language model
agent = initialize_agent(tools, llm, agent='zero-shot-react-description', verbose=True)


# Define an endpoint 
@app.get('/question')
def prompt(question: str):
    # Invoke the agent with the provided question
    result = agent.invoke(question)
    return {'output': result}

# Entry point for running the FastAPI application with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
