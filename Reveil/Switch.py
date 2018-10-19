import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin_switch=[19,21]

S_amp = pin_switch[0]
S_tuner = pin_switch[1]

for i in pin_switch :
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

def Amp():
    GPIO.output(S_amp, GPIO.LOW)
    time.sleep(0.09)
    GPIO.output(S_amp, GPIO.HIGH)

def Tuner():
    GPIO.output(S_tuner, GPIO.LOW)
    time.sleep(0.09)
    GPIO.output(S_tuner, GPIO.HIGH)


