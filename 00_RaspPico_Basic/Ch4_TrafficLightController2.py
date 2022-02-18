import machine
import utime
import _thread


red_light = machine.Pin(15, machine.Pin.OUT)
yellow_light = machine.Pin(14, machine.Pin.OUT)
green_light = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(1, machine.Pin.OUT)

# while True:
#     if button.value() == 1:
#         print("You've pressed the button")
#         utime.sleep(1)
        
global button_pressed
button_pressed = False

def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.01)
    _thread.start_new_thread(button_reader_thread, ())
    

while True:
    if button_pressed == True:
        red_light.value(1)
        for i in range(10):
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)
        global button_pressed
        button_pressed = False
    buzzer.value(1)
    buzzer.value(0)
    red_light.value(5)
    utime.sleep(1)
    red_light.value(0)
    yellow_light.value(1)
    utime.sleep(1)
    yellow_light.value(0)
    green_light.value(2)
    utime.sleep(1)
    green_light.value(0)
    