#  _____   __     __  ___     _____   __  __    _____ 
# |  __ \  \ \   / / |__ \   / ____| |  \/  |  / ____|
# | |__) |  \ \_/ /     ) | | (___   | \  / | | (___  
# |  ___/    \   /     / /   \___ \  | |\/| |  \___ \ 
# | |         | |     / /_   ____) | | |  | |  ____) |
# |_|         |_|    |____| |_____/  |_|  |_| |_____/ 
#                                                     
                                                   

import requests
# 'pip install requests' to install this library

def sms(pnumber,msg):
  addr = "http://textbelt.com/text"
  number = str(pnumber)
  message= str(msg)
  r = requests.post(addr,data={'number' : number, 'message' : message})
  if r.status_code == 200:
    print("Message: " + msg + " sent to phone number: " + str(pnumber))
  else:
    print("Message: " + msg + " failed to send to phone number: " + str(pnumber))

# To send a text message call the function with
# sms(phonenumber,'sending this text message')
# sms(5551235555,'Hello World!')
