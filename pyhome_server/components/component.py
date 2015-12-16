
import abc
# RPi needs to raspberry pi to run
# import RPi.GPIO as GPIO

class Component:

    __metaclass__ = abc.ABCMeta

    def __init__(self, **bcm_gpio_pins):
        # GPIO.setmode(GPIO.BCM)
        for pin, number in bcm_gpio_pins.iteritems():
            setattr(self, pin, number)
