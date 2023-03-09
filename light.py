
print("Welcome to my First Project")
from microbit import *

while True:
    if button_a.is_pressed():
        pin0.write_digital(1)
        sleep(2000)
    else:
        pin0.write_digital(0)
