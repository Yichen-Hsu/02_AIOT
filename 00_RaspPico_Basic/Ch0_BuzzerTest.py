import machine
import _thread
import utime

buzzer = machine.Pin(1, machine.Pin.OUT)

while True:
    buzzer.value(1)
    utime.sleep(1)