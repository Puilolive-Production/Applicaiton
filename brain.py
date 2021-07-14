import eel
import sys
import os 
import json
sys.path.append('..')
sys.path.append(os.getcwd())
import config 
import face.face_recognition_windows

config.init()

# Some temps
usrname_temp = ""
usrAge_temp = 0
usrHeight_temp = 0.0
usrCurrentWeight_temp = 0.0
usrGender_temp = ""
usrSMM_temp = 0.0

# Loading JSON file
with open(os.getcwd()+r"\user_infos.json", 'r') as f:
    data = json.loads(f.read()) #data becomes a dictionary

# Initing eel
eel.init(os.getcwd() + '\web') 
eel.start('main.html', block=False)


# Some eel functions
@eel.expose
def send_usrname(msg):
    print("Received usrname: " + msg)
    global usrname_temp
    usrname_temp = msg
    print("usrname_temp: " + usrname_temp)
    return "ok"

@eel.expose
def send_usrAge(msg):
    print("Received usrAge: " + msg)
    global usrAge_temp
    usrAge_temp = msg
    print("usrAge_temp: " + usrAge_temp)
    return "ok"

@eel.expose
def send_usrHeight(msg):
    print("Received usrHeight: " + msg)
    global usrHeight_temp
    usrHeight_temp = msg
    print("usrHeight_temp: " + usrHeight_temp)
    return "ok"

@eel.expose
def send_usrCurrentWeight(msg):
    print("Received usrCurrentWeight: " + msg)
    global usrCurrentWeight_temp
    usrCurrentWeight_temp = msg
    print("usrCurrentWeight_temp: " + usrCurrentWeight_temp)
    return "ok"

@eel.expose
def send_usrGender(msg):
    print("Received usrGender: " + msg)
    global usrGender_temp
    usrGender_temp = msg
    print("usrGender_temp: " + usrGender_temp)

@eel.expose
def send_usrSMM(msg):
    print("Received usrSMM: " + msg)
    global usrGender_temp
    usrSMM_temp = msg
    print("usrSMM_temp: " + usrSMM_temp)

    # Add usrname and all items back to the JSON file
    usrDataArr_temp = {"usrAge": usrAge_temp, "usrHeight": usrHeight_temp, "usrCurrentWeight": usrCurrentWeight_temp, "usrGender": usrGender_temp, "usrSMM": usrSMM_temp}
    data[usrname_temp] = usrDataArr_temp
    with open(os.getcwd()+r"\user_infos.json", 'w') as json_file:
        json.dump(data, json_file)

    return "ok"    

@eel.expose
def send_currentUsrname():
    print(config.loged_in_usrname)
    return config.loged_in_usrname

@eel.expose
def send_currentUsrinfo():
    print(config.loged_in_usrname)
    currentusrAge = data[str(config.loged_in_usrname)]["usrAge"]
    print(currentusrAge)
    currentusrHeight = data[str(config.loged_in_usrname)]["usrHeight"]
    print(currentusrHeight)
    currentusrCurrentWeight = data[str(config.loged_in_usrname)]["usrCurrentWeight"]
    print(currentusrCurrentWeight)
    currentusrGender = data[str(config.loged_in_usrname)]["usrGender"]
    print(currentusrGender)
    currentusrSMM = data[str(config.loged_in_usrname)]["usrSMM"]
    print(currentusrSMM)
    currentusrInfo_Arr = [currentusrAge, currentusrHeight, currentusrCurrentWeight, currentusrGender, currentusrSMM]
    return currentusrInfo_Arr



while True:
    eel.sleep(2000.0)