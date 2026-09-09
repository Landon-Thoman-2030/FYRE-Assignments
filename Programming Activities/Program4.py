# Blinking Program

# incoporate/include module
import machine #adding machine module
import time #adding time module
# Make the led object
led = machine.Pin(0, machine.Pin.OUT) #varible of the led
# Infinite Loop
while True:
  led.value(1) # turns led on
  time.sleep(0.25) #.25 second delay
  led.value(0) #turn led off
  time.sleep(0.25) #.25 second delay


