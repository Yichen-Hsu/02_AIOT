import machine
import utime
from machine import Pin, PWM

servo = PWM(Pin(0))
servo.freq(50)
sensor = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)

def pin_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("detected")
        servo.duty_u16(6500)
        utime.sleep(3)
        servo.duty_u16(8200)
        utime.sleep(0.5)        
        

sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=pin_handler)

while True:
    led.toggle()
    utime.sleep(5)