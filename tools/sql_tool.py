

from langchain.tools import QuerySQLDatabaseTool
from langchain_openai import ChatOpenAI
from langchain.sql_database import SQLDatabase

llm = ChatOpenAI(model= 'gpt-3.5-turbo', temperature= 0)
db = SQLDatabase.from_uri('sqlite:///northwind.db')

sql_tool = QuerySQLDatabaseTool(db= db, llm= llm)


