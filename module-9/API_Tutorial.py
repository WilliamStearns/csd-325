#William Stearns
#4-21-25
#Module 9.2
#This program is for going through a tutorial on APIs.

import requests
import json 

response = requests.get("http://api.open-notify.org/astros.json")
#print(response.status_code)
#print(response.json())

def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

jprint(response.json())