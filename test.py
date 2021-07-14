import os 
import json

with open(os.getcwd()+r"\user_infos.json", 'r') as f:
    data = json.loads(f.read()) #data becomes a dictionary

print(data["Testing"]["usrAge"])