import sys
import os 

sys.path.append(os.getcwd())

print(os.getcwd())
print(os.path.isdir(os.getcwd()))
print(os.path.isfile("user_infos.json"))