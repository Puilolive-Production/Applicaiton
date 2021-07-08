import eel
import sys
import os 
# sys.path.append('/.../login')
# import login
sys.path.append('..')
sys.path.append(os.getcwd())
import face.face_recognition_windows

# needs to change the path whenever switching to a new environment
eel.init(os.getcwd() + '\\ui\web') 
eel.start('main.html', block=False)

@eel.expose
def send_usrname(msg):
    print("Received usrname: " + msg)
    user_name = msg
    return "ok"

@eel.expose
def send_usrAge(msg):
    print("Received usrAge: " + msg)
    return "ok"

@eel.expose
def send_usrHeight(msg):
    print("Received usrHeight: " + msg)
    return "ok"

@eel.expose
def send_usrCurrentWeight(msg):
    print("Received usrCurrentWeight: " + msg)
    return "ok"

@eel.expose
def send_usrIdealWeight(msg):
    print("Received usrIdealWeight: " + msg)
    return "ok"

while True:
    eel.sleep(2000.0)