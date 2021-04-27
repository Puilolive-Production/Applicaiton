from login.login import *
from face_recognition.face_recognition import *

choice = sl_choice()

if choice.capitalize() == 'S':
    user_name = signup()
    input_faces(user_name)

if choice.capitalize() == 'L':
    user_name = login()
    