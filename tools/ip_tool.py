

import requests
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool

class IPInfo(BaseModel):
    ip_address: str = Field(description = "ip address")
    
def fetch_ip_info(ip_address : str) -> str:
    url = f'https://ipapi.co/{ip_address}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data

ip_info_tool = StructuredTool.from_function(func= fetch_ip_info, 
                                            name= 'IP adress info',
                                            description= 'fetch ip address information from ipapi.co',
                                            args_schema= IPInfo, 
                                            return_direct= True)