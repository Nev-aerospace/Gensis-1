
#    Nev Aerospace flight controller built for the raspberry PI ecosystem
#     Copyright (C) 2022  StoneMcYT (https://github.com/StoneMcYT)

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

##############################################
# IMPORT EVERYTHING #
##############################################
# Sense hat declration

from time import sleep
import os
from gpiozero import CPUTemperature
import json
import random
from sense_hat import SenseHat
import db

sense = SenseHat()

# cmd = './ngrok tcp 22'

# os.system(cmd)


# Extra Var stuff
DataSendTime = 0


with open("./config.json"
          "w") as jsonfile:
    data = json.dump(jsonfile)
print(data)

# Sense
#  Hat Deffs for Temp + pressure + humid
temp = sense.get_temperature()
pressure = sense.get_pressure()
humidity = sense.get_humidity()

# Mesure


def MesFromHat():
    print(temp)
    print(pressure)
    print(humidity)

def gyroReadOut():






# ############################################## - DISABLED FOR NOW TILL STAGE 2 OR 3
# # Twilio MQTT Demo for Programmable Wireless #
# ##############################################
# from time import sleep
# from sys import exit
# from smbus import SMBus
# import json
# import paho.mqtt.client as mqtt
# from twilio.rest import Client
# Twillo stuff
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)


# Cpu Temp Checker
cpu = CPUTemperature()


#  Pre Launch Stats -  CPU temp + Display Led check + altitube + other things
def LaunchSat():
    print("Welcome to", ModelName + "Python based control module")
    print("The current CPU temp is", cpu.temperature)
    print("HAT MODULE TEST SHALL START")
    print("Displaying random number as display test seqence....")
    x = random(1, 100)
    print(x)
    sense.show_message(x)
    print("Completed  please check LED for issues")

    print("Gyroscopic data readout")
    print(MesFromHat())

# Preflight checks USE: Count down at launch flight - Might incdlue some preflight altitube and gyrocopial analysis later


def PreFlight():
    sense.show_message("FLIGHT SHALL START:")
    x = 30
    sense.show_message("T-")
    while x != -1:
        print("T-", x)
        x -= 1
        sleep(1)
        sense.show_message(x)
    print("Lift off")


# Sending Interval check - PRE PRE PRE
def PreDataSend():
    DataSendTime = 0
    DataSendTime = int(
        input("Data Checking Launched set data post int in seconds: "))
    while DataSendTime <= 0 or DataSendTime >= 20:
        print("You sure you placed it corecct?")
        DataSendTime = int(
            input("Data Checking Launched set data post int in seconds: "))










# Call all the func bellow