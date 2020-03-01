import logging
from RPi import GPIO


class SwitchIndicator:

    def __init__(self, gpio_pin):
        
        # logging configuration
        self.__logger = logging.getLogger(__name__)
        self.__logger.info("Creating new LED instance at GPIO pin '%i'" % int(gpio_pin))
        
        # GPIO setup
        self.__pin = int(gpio_pin)
        GPIO.setup(self.__pin, GPIO.OUT)

    @property
    def on(self):
        return GPIO.input(self.__pin)

    def turn_on(self):
        self.__logger.info("Turning on led at GPIO %s" % self.__pin)
        GPIO.output(self.__pin, GPIO.HIGH)

    def turn_off(self):
        self.__logger.info("Turning off led at GPIO %s" % self.__pin)
        GPIO.output(self.__pin, GPIO.LOW)

    def toggle(self):
        if self.on:
            self.turn_off()
        else:
            self.turn_on()
