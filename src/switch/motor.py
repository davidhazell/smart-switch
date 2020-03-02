import logging
import time
from RPi import GPIO


class SwitchMovement:

    def __init__(self, gpio_pin):

        # Logging configuration
        self.__logger = logging.getLogger(__name__)
        self.__logger.info("Creating new motor instance at GPIO pin '%i'" % int(gpio_pin))

        # ToDo: GPIO setup
        self.__pin = int(gpio_pin)
        GPIO.setup(self.__pin, GPIO.LOW)
        self.__motor_power_interval = .001

    def activate(self):
        GPIO.output(self.__pin, GPIO.HIGH)
        time.sleep(self.__motor_power_interval)
        GPIO.output(self.__pin, GPIO.LOW)

