##############################################
# IMPORT EVERYTHING #
##############################################
#Sense hat declration
from sense_hat import SenseHat
sense = SenseHat()

##############################################
# Twilio MQTT Demo for Programmable Wireless #
##############################################
from time import sleep
from sys import exit
from smbus import SMBus
import json
import paho.mqtt.client as mqtt








#Sense hat wake up
sense.show.message("HAT is connected)
