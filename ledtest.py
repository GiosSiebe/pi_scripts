import time
import wiringpi
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1) # Schrijf 1 (Hoog) naar pin
    time.sleep(0.5)
    wiringpi.digitalWrite(_pin, 0) # Schrijf 1 (Hoog) naar pin
    time.sleep(0.5)

#SETUP
print("Start")
pin = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1) #Set pin to mode 1 (OUTPUT)

#MAIN
for i in range(0,10):
    blink(pin)

#cleanup
print("Done")