# Turn lights on and off based on song timestamps

import playsound
import config
import requests
from time import sleep

bridge_ip = config.bridge_ip
user = config.username

url = 'http://' + bridge_ip + '/api/' + user +  '/lights/2/state'

def setLights(opt):
	requests.put(url, json={"on": opt})

playsound.playsound("Music/luz.mp3", block=False)

sleep(24) # 00:24

print("Fua!")
setLights(False)

sleep(2) # 00:26

print("Back!")
setLights(True)

sleep(2) # 00:28

print("Fua!")
setLights(False)

sleep(2) # 00:30

print("Back!")
setLights(True)