import unittest
from time import sleep
from pyhome_server.components.relay import Relay
import RPi.GPIO as GPIO


class RelayTestCase(unittest.TestCase):
    def setUp(self):
        """To test relay, a relay must be connected with the control pins
        conected and another set of pins connected to the switching side of
        the relay"""
        self.test_pin = {'control_pin', 5}
        self.instance = Relay(**self.test_pin)
        self.common_terminal_pin = 9
        self.normaly_open_pin = 10
        self.normaly_closed_pin = 11
        GPIO.setup(self.common_terminal_pin, GPIO.OUT)
        GPIO.setup(self.normaly_open_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.normaly_closed_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def test_control_pin_set_on_init(self):
        """Test that the relay contol pin can be set when the class is
        instantiated"""
        self.assertEqual(self.instance.control_pin, self.test_pin['control_pin'])

    def test_the_control_pin_is_output(self):
        """Test that the relay control pin is set to an output during init"""
        returned = GPIO.gpio_function(self.test_pin['control_pin'])
        self.assertEqual(returned, GPIO.OUT)

    def test_relay_state_functions(self):
        """Since the relay cannot be stateless, its tests must occur in order
        - Default State test
            Test that the default_state is with the normaly closed terminal,
            connected to the common terminal and the normally open terminal
            disconnected
        - On State test
            Test that the on method, connects the normally open terminal and
            disconnects the normally closed terminal
        -Off State test
            Test that the off method, when called after the on method
            disconnects the normally open terminal and connects the normally
            closed terminal
        """

        GPIO.output(self.common_terminal_pin, GPIO.LOW)
        self.assertEqual(GPIO.input(self.normaly_closed_pin), GPIO.LOW)
        self.assertEqual(GPIO.input(self.normaly_open_pin), GPIO.LOW)
        GPIO.output(self.common_terminal_pin, GPIO.HIGH)
        self.assertEqual(GPIO.input(self.normaly_closed_pin), GPIO.LOW)
        self.assertEqual(GPIO.input(self.normaly_open_pin), GPIO.HIGH)

        self.instance.on()
        sleep(0.5)  # Switching time for relay is about 150ms
        GPIO.output(self.common_terminal_pin, GPIO.LOW)
        self.assertEqual(GPIO.input(self.normaly_closed_pin), GPIO.LOW)
        self.assertEqual(GPIO.input(self.normaly_open_pin), GPIO.LOW)
        GPIO.output(self.common_terminal_pin, GPIO.HIGH)
        self.assertEqual(GPIO.input(self.normaly_closed_pin), GPIO.LOW)
        self.assertEqual(GPIO.input(self.normaly_open_pin), GPIO.HIGH)

        self.instance.off()
        sleep(0.5)  # Switching time for relay is about 150ms
        GPIO.output(self.common_terminal_pin, GPIO.LOW)
        self.assertEqual(GPIO.input(self.normaly_closed_pin), GPIO.LOW)
        self.assertEqual(GPIO.input(self.normaly_open_pin), GPIO.LOW)
        GPIO.output(self.common_terminal_pin, GPIO.HIGH)
        self.assertEqual(GPIO.input(self.normaly_closed_pin), GPIO.LOW)
        self.assertEqual(GPIO.input(self.normaly_open_pin), GPIO.HIGH)
