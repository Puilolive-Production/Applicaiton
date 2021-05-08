import cv2
import sys 
import os
sys.path.append(os.path.abspath("/face"))
from face.face_recognition_windows import input_faces, face_recogn
import ntpath

def sl_choice():
    boool = False
    while boool == False:
        choice = input('Login (L) or Sign up (S)? ')
        if choice.capitalize() == 'L' or choice.capitalize() == 'S':
            boool = True
            return choice
        
def signup():
    user_name = input('Please enter your username: ')
    disclaim_bool = False
    while disclaim_bool == False:
        disclaim = input('We need your photos for analyzing. Would you mind us taking a picture of you? (Y/N) ')
        if disclaim.capitalize() == "Y":
            input_faces(user_name)
    return user_name
        
def login():
    user_name = ntpath.basename(str(face_recogn()))[:-4]
    print(user_name)
