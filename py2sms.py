#  _____   __     __  ___     _____   __  __    _____ 
# |  __ \  \ \   / / |__ \   / ____| |  \/  |  / ____|
# | |__) |  \ \_/ /     ) | | (___   | \  / | | (___  
# |  ___/    \   /     / /   \___ \  | |\/| |  \___ \ 
# | |         | |     / /_   ____) | | |  | |  ____) |
# |_|         |_|    |____| |_____/  |_|  |_| |_____/ 
#                                                     


import json
import pprint
import requests
# 'pip install requests' to install this library


with open('credentials','r') as c:
		cred = c.readlines()

def sms(pnumber,msg):
	addr = "https://app.eztexting.com/sending/messages?format=json"
	number = str(pnumber)
	message= str(msg)
	content = {
		'User': cred[0].strip(), 
		'Password': cred[1].strip(),
		'PhoneNumbers[]': number,
		'Message': message}
	pprint.pprint(content)
	r = requests.post(addr,data=content)
	if r.status_code != 204:
		pprint.pprint(r.json())
	else:
		print("Status code 204: No content returned")

# To send a text message call the function with
# sms(phonenumber,'sending this text message')
# sms(5551235555,'Hello World!')