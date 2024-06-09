"SQL Tool for interacting with the northwind database"

# Import necessary libraries
from langchain_openai import ChatOpenAI
from langchain.tools import QuerySQLDataBaseTool
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Initialize the language model
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature= 0.5)

# Initialize the SQL database
db = SQLDatabase.from_uri('sqlite:///northwind.db')

# Define the SQL tool for querying the database
sql_tool = QuerySQLDataBaseTool(db=db, llm= llm, description= 'use this tool to query the northwind database')
 

