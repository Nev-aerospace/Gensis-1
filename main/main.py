##############################################
# IMPORT EVERYTHING #
##############################################
#Sense hat declration
from sense_hat import SenseHat
sense = SenseHat()
temp = sense.get_temperature()
pressure = sense.get_pressure()
humidity = sense.get_humidity()
import time 
#OS Stuff


import os
cmd = './ngrok tcp 22'
os.system(cmd)
# ##############################################
# # Twilio MQTT Demo for Programmable Wireless #
# ##############################################
# from time import sleep
# from sys import exit
# from smbus import SMBus
# import json
# import paho.mqtt.client as mqtt


#Cpu Temp Checker
from gpiozero import CPUTemperature
cpu = CPUTemperature()



import os
from twilio.rest import Client


#Var declars
model = "ModelName"
owner = "Nev Aerospace"
returnadd = "Return adress"


#Twillo stufff
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


#INtro
print("Welcome to", model + "Python bassed control module")

#CPU Print
print(cpu.temperature)
#PRINT THE Stuff into what not
def mesFromHat():
  print(Sense.temp)
  print(Sense.pressure)
  print(Sense.humidity)
#Sense hat wake up
sense.show.message("HAT is connected")
sense.show.message("anddd nev is a furry")
           
                   
while x == True:
  mesFromHat()
  time.sleep(30)
