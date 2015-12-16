
import abc

class Component:

    __metaclass__ = abc.ABCMeta

    def __init__(self, **bcm_gpio_pins):
        for pin, number in bcm_gpio_pins.iteritems():
            setattr(self, pin, number)
