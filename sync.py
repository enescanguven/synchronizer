import os
import time 
import json

json_file=open('conf.json') 
data = json.load(json_file)

command_sync = 'rsync -a --progress '
local_dir = data["local_dir"]
remote_dir = data["remote_dir"]
remote_copy_dir = data["remote_copy_dir"]
local_copy_dir = data["local_copy_dir"]
remote_user = data["remote_user"]

print('Transfer starting')
print("Sending...")

command_send = command_sync+local_dir+remote_user+ remote_dir
os.system(command_send)

print("Downloading")

command_get = command_sync+remote_user+remote_copy_dir+ " "+local_copy_dir
os.system(command_get)

time.sleep(1)

print('Transfer Compeleted')
