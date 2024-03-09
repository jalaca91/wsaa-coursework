# Author: Jaime Lara Carrillo
# this program retrieves the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json"

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def getAPI():
    response = requests.get(url)
    if response.status_code == 200:   # verifies if the request is successful
        data =  response.json()
        with open("cso.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Data created :", "cso.json")

getAPI()