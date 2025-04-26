#William Stearns
#4-26-25
#Module 9.2
#This program connects to an Api and retrieves data from it, displaying status code, unformatted and formatted data.

import requests
import json 

def json_print(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print("\nFormatted JSON Response: \n")
    print(text) 

def main():
    response = requests.get("https://pokeapi.co/api/v2/pokemon-species?limit=3") #limited for screen space. 

    print(f"\nStatus Code: \n{response.status_code}\n") #Display status code
    print("Unformatted JSON Response: \n")
    print(response.json()) #Display unformatted data
    json_print(response.json()) #Display formatted data
if __name__ == "__main__":
    main()