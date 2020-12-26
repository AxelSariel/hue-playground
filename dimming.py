import requests
import config
from time import sleep

bridge_ip = config.bridge_ip
user = config.username

url = 'http://' + bridge_ip + '/api/' + user +  '/lights/2/state'

for i in range(1, 65535, 500):
	body = {
		"on" : True,
		"bri" : 254,
		"hue" : i
	}

	response = requests.put(url, json=body)
	print(response.json()[0], i)

	sleep(.2)