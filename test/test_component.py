from pyhome_server.components.component import Component

import unittest

class ComponentTestCase(unittest.TestCase):

    def setUp(self):
        self.test_pin_info = {'a': 1, 'b': 3, 'c': 37, 'f': 'another property'}

    def test_component_sets_pins_on_init(self):
        """Tests that when initialised, component passes the initialisation
        kwargs into properties of the class"""
        instance = Component(**self.test_pin_info)
        self.assertEqual(instance.a, self.test_pin_info['a'])
        self.assertEqual(instance.b, self.test_pin_info['b'])
        self.assertEqual(instance.c, self.test_pin_info['c'])
        self.assertEqual(instance.f, self.test_pin_info['f'])

    def test_component_only_sets_pins_on_init(self):
        """Test that attributes arent set in a way that means default values
        are returned for unset attributes"""
        instance = Component(**self.test_pin_info)
        with self.assertRaises(AttributeError):
            instance.d
        with self.assertRaises(AttributeError):
            instance.e

