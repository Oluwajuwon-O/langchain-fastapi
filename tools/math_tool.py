

from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model= 'gpt-3.5-turbo', temperature= 0)

math_chain = LLMMathChain.from_llm(llm= llm)
math_tool = Tool.from_function(name= "math calculator",
                               func= math_chain.run, 
                               description= "For answering all math questions.\
                                   It can also be used with other tools\
                                       but only in aspects that involve maths")
