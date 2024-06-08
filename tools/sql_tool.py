
from langchain.agents import initialize_agent
from langchain.tools import QuerySQLDataBaseTool
from langchain_openai import ChatOpenAI
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model= 'gpt-3.5-turbo', temperature= 0)
with SQLDatabase.from_uri('sqlite:///northwind.db') as db:
    sql_tool = QuerySQLDataBaseTool(db= db, llm= llm)


agent = initialize_agent(sql_tool, llm, agent='zero-shot-react-description', verbose=True)
print(agent.invoke('How many suppliers does northwind have?'))

engine = db.engine
engine.dispose()
