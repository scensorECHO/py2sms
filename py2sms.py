#  _____   __     __  ___     _____   __  __    _____ 
# |  __ \  \ \   / / |__ \   / ____| |  \/  |  / ____|
# | |__) |  \ \_/ /     ) | | (___   | \  / | | (___  
# |  ___/    \   /     / /   \___ \  | |\/| |  \___ \ 
# | |         | |     / /_   ____) | | |  | |  ____) |
# |_|         |_|    |____| |_____/  |_|  |_| |_____/ 
#                                                     


import requests

# 'pip install requests' to install this library


with open('credentials','r') as c:
	try:
		cred = c.readlines()
	except:
		print("File could not be read")
		exit()


def sms(pnumber,msg):
	addr = "https://app.eztexting.com/sending/messages?format=format"
	number = str(pnumber)
	message= str(msg)
	r = requests.post(addr,data={
		'User' : cred[0], 
		'Password' : cred[1]
		'PhoneNumbers' : [number]
		'Message' : message})
	# if r.status_code != 204:
	# 	if r.json()["success"]:
	# 		print("Message: \"" + msg + "\" sent to phone number: " + str(pnumber))
	# 	else:
	# 		print("Message failed: "+str(r.json()["message"]))
	# else:
	# 	print("Status code 204: No content returned")

# To send a text message call the function with
# sms(phonenumber,'sending this text message')
# sms(5551235555,'Hello World!')