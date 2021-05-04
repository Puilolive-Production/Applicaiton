import cv2
import sys 
import os
sys.path.append(os.path.abspath("/face_recognition_part"))
from face_recognition_part.face_recogn import input_faces

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
    login_choice = input('Login with (F) ace detection or (P) assword? ')
    if login_choice.capitalize() == "F":
        user_name = input('Please enter your username: ')
        return user_name
    elif login_choice.capitalize() == "P": 
        user_name = input('Please enter your username: ')
        user_password = input('Please enter your password: ')
