import machine
import utime

red_light = machine.Pin(15, machine.Pin.OUT)
yellow_light = machine.Pin(14, machine.Pin.OUT)
green_light = machine.Pin(13, machine.Pin.OUT)

while True:
    red_light.value(5)
    utime.sleep(1)
    red_light.value(0)
    yellow_light.value(1)
    utime.sleep(1)
    yellow_light.value(0)
    green_light.value(2)
    utime.sleep(1)
    green_light.value(0)