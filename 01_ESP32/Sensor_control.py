from machine import Pin
import utime

sensor1 = Pin(13, Pin.IN, Pin.PULL_DOWN)

def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        if pin is sensor1:
            print("detected!")


sensor1.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)
