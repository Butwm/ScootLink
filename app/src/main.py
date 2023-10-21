import time
import requests
import json
import datetime

url = "https://apiflask.alge1352.repl.co/"
online = True
local_time = datetime.datetime.now()
def get_api_data():
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            jsonString = json.dumps(data)
            jsonFile = open("data.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()

while online == True:
    get_api_data()
    print("Writed to data.json at: ", local_time)
    time.sleep(240)
