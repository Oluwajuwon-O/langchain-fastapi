


from langchain_openai import ChatOpenAI
from langchain.tools import QuerySQLDataBaseTool
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Initialize the language model
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)

# Initialize the SQL database
db = SQLDatabase.from_uri('sqlite:///northwind.db')
sql_tool = QuerySQLDataBaseTool(db=db, llm= llm)

