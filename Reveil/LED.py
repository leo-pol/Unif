import RPi.GPIO as GPIO
import pigpio
import os
import time

pi=pigpio.pi()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Inter=12

E_inter=1
A_loop=False

GPIO.setup(Inter, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def led(pin,val):
    pi.set_PWM_dutycycle(pin,val)

while True:
    if GPIO.input(Inter)==0:
        E_inter += 1
        A_loop = True
        time.sleep(0.2)

    if E_inter%2 == 0 and A_loop:
        A_loop = False
        led(17, 255)
    elif A_loop:
        A_loop = False
        led(17,0)
