from machine import Pin
import utime

ENA = Pin(16, Pin.OUT)
N1 = Pin(17, Pin.OUT)
N2 = Pin(5, Pin.OUT)

while True:
    ENA.value(0)
    N1.value(1)
    N2.value(0)