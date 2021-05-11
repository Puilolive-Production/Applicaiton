from deepface import DeepFace
import cv2
import time
import os
import numpy as np
from PIL import Image, ImageDraw
from IPython.display import display
import pandas as pd
from pathlib import Path



# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(1)

def input_faces(user_name):
    # Define a video capture object
    start_time = time.time()

    path = 'face/known_pics'
    while(True):
        # Capture the video frame by frame
        ret, frame = video_capture.read()
        
        if time.time() - start_time >= 4: # <-- Check if 3 sec passed
            img_name = os.path.join(path, "{}.png".format(user_name))
            if frame is not None:
                cv2.imwrite(img_name, frame)
                print("{} written!".format(user_name))
                break
            else:
                print('Error: frame is none')
                break
    # After the loop release the cap object
    video_capture.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    # Load a sample picture and learn how to recognize it.
    result  = DeepFace.find(img_path="{}.png".format(user_name), db_path="face/known_pics")

def face_recogn():
    # Define a video capture object
    start_time = time.time()
    path = 'face/unknown_face'
    while(True):
        # Capture the video frame by frame
        ret, frame = video_capture.read()
        
        if time.time() - start_time >= 4: # <-- Check if 3 sec passed
            img_name = os.path.join(path, "unknown_img.png")
            if frame is not None:
                cv2.imwrite(img_name, frame)
                print("unknown face img written!")
                break
            else:
                print('Error: frame is none')
                break

    video_capture.release()
    cv2.destroyAllWindows()
    df = DeepFace.find(img_path = "face/unknown_face/unknown_img.png", db_path = 'face/known_pics')
    if df.shape[0] > 0:
        matched = df.iloc[0].identity
        print(matched)
    return matched
        

# input_faces("Peter")