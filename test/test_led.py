import unittest
import logging.config
import time
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from RPi import GPIO
from src.switch.led import SwitchIndicator


class TestSwitchIndicator(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSwitchIndicator, self).__init__(*args, **kwargs)

        # Logging
        logging.config.fileConfig("config/logging.config")
        self.logger = logging.getLogger(__name__)
        self.logger.info('TestSwitchIndicator')

        # GPIO
        GPIO.setmode(GPIO.BCM)
        self.__gpio_pin = 27

    def test_create_instance(self):
        s = SwitchIndicator(gpio_pin=self.__gpio_pin)

    def test_get_on_status(self):
        s = SwitchIndicator(gpio_pin=self.__gpio_pin)

    def test_power_on_and_off(self):
        s = SwitchIndicator(gpio_pin=self.__gpio_pin)

        for _ in range(0,10):
            s.turn_on()
            time.sleep(.25)
            s.turn_off()
            time.sleep(.25)
