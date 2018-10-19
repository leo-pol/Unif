import datetime
import RPi.GPIO as GPIO
import pigpio
import os
import time
import math
import Switch

pi=pigpio.pi()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

"""###############################################################################
PARTIE LED
###############################################################################
"""
rouge=17
vert=22
bleu=24

def led(couleur,val):
    pi.set_PWM_dutycycle(couleur,val)

def led_off():
    for i in [rouge,vert,bleu]:
        led(i,0)
def led_rgb(red,green,blue):
    led(rouge,red)
    led(vert,green)
    led(bleu,blue)

"""#############################################################################
AVOIR LE TEMPS 
##############################################################################"""

temps=datetime.datetime.now()
Ntemps=str(temps)
Ftemps=Ntemps.split()
date=Ftemps[0]
time=Ftemps[1]

jour = int(date[8:])
mois = int(date[5:7])
heure = int(time[:2])
minute = int(time[3:5])
seconde = int(time[6:8])
print (jour, "/", mois)
print(heure,minute,seconde)

"""#############################################################################
#############################################################################"""

