


from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.tools import QuerySQLDataBaseTool
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv



# Load environment variables
load_dotenv()

# Initialize the language model
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)

# Initialize the SQL database
db = SQLDatabase.from_uri('sqlite:///northwind.db')
sql_tool = QuerySQLDataBaseTool(db=db, llm= llm, description= 'use this tool to query the northwind database')
 

