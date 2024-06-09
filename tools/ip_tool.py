'''
IP Address Tool for fetching IP information about IP addresses from ipapi.co
No authentication required
'''


# import libraries
import requests
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool

# Define the schema for the IP information request
class IPInfo(BaseModel):
    ip_address: str = Field(description = "ip address")

# Function to fetch IP information from ipapi.co    
def fetch_ip_info(ip_address : str) -> str:
    url = f'https://ipapi.co/{ip_address}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
      return f"Error: Unable to fetch data for IP {ip_address}"

# Define the IP information tool using StructuredTool
ip_info_tool = StructuredTool.from_function(func= fetch_ip_info, 
                                            name= 'fetch information on the IP address supplied',
                                            description= 'fetch ip address information from ipapi.co',
                                            args_schema= IPInfo, 
                                            return_direct= True)