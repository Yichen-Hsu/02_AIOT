import machine
import utime

button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        print("You Preesed the Button!")
#         utime.sleep(2)