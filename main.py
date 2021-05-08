import sys 
import os
from login.login import *
from face.face_recognition_windows import *

sys.path.append(os.path.abspath("/face"))

# User choose to login or sign up
choice = sl_choice()

if choice.capitalize() == 'S':
    user_name = signup()
elif choice.capitalize() == 'L':
    user_name = login()
