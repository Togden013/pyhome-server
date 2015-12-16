
import unittest
from pyhome_server.components.relay import Relay


class RelayTestCase(unittest.TestCase):

    def test_control_pin_set_on_init(self):
        """Test that the relay contol pin can be set when the class is
        instantiated"""
        instance= Relay(control_pin=5)
        self.assertEqual(instance.control_pin, 5)
