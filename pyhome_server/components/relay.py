from pyhome_server.components.component import Component
import RPi.GPIO as GPIO


class Relay(Component):
    def __init__(self, control_pin=None):
        super(Relay, self).__init__(control_pin=control_pin)
        GPIO.setup(control_pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.control_pin, GPIO.LOW)

    def off(self):
        GPIO.output(self.control_pin, GPIO.HIGH)
