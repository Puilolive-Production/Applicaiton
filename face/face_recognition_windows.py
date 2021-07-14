from deepface import DeepFace
import cv2
import time
import os
import eel
import numpy as np
from PIL import Image, ImageDraw
from IPython.display import display
import pandas as pd
from pathlib import Path
import config

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

@eel.expose
def input_faces(user_name):
    path = os.getcwd() + r"\face\known_pics\{}".format(user_name)
    os.mkdir(path)
    
    ret, frame = video_capture.read()
    d = 0

    while ret:
        img_path = os.path.join(path, "{}_.png".format(user_name + "_" + str(d)))
        cv2.imwrite(img_path, frame)
        d+=1  
        if d == 3:
            break  
    
    video_capture.release()
    cv2.destroyAllWindows()
    config.loged_in_usrname = user_name

    return "ok"

@eel.expose
def face_recogn():
    path_known_pics = os.getcwd() + r"\face\known_pics"
    
    retval, frame = video_capture.read()
    img_path = os.getcwd() + r"\face\unknown_face\unknown_img.png"
    if retval != True:
        raise ValueError("Can't read frame")
        
    cv2.imwrite(img_path, frame)
    cv2.imshow("unknown_img", frame)
    # cv2.waitKey()
    video_capture.release()
    cv2.destroyAllWindows()

    if (os.path.isfile("G:\\Shared drives\\Puilolive Production\\Applicaiton\\face\\known_pics\\representations_vgg_face.pkl") == True):
        os.remove(os.getcwd() + r"\face\known_pics\representations_vgg_face.pkl")
    
    df = DeepFace.find(img_path = img_path, db_path = path_known_pics)
    if df.shape[0] > 0:
        matched = df.iloc[0].identity
        print(matched)
        global loged_in_usrname
        loged_in_usrname = os.path.basename(matched)[:-7]
        print("logged in username:", loged_in_usrname)
        config.loged_in_usrname = loged_in_usrname
    
    return "ok"
