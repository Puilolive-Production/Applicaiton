from login.login import *
import sys 
import os
sys.path.append(os.path.abspath("/face_recognition_part"))
from face_recognition_part.face_recogn import *

# User choose to login or sign up
choice = sl_choice()

if choice.capitalize() == 'S':
    user_name = signup()
elif choice.capitalize() == 'L':
    user_name = login()
