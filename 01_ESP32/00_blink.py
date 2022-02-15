from machine import Pin

led = Pin(2, Pin.OUT)
led.on()

from time import sleep
while True:
    sleep(1)
    led.off()
    sleep(1)
    led.on()