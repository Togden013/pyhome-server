
import unittest
from pyhome_server.components.relay import Relay
# RPi needs to raspberry pi to run
# import RPi.GPIO as GPIO


class RelayTestCase(unittest.TestCase):

    def test_control_pin_set_on_init(self):
        """Test that the relay contol pin can be set when the class is
        instantiated"""
        instance= Relay(control_pin=5)
        self.assertEqual(instance.control_pin, 5)

    # def test_the_control_pin_is_output(self):
    #     """Test that the relay control pin is set to an output during init"""
    #     test_pin = {'control_pin', 5}
    #     instance = Relay(**test_pin)
    #     returned = GPIO.gpio_function(test_pin['control_pin'])
    #     self.assertEqual(returned, GPIO.OUT)