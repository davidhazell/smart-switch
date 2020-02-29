import logging
from RPi import GPIO
from hardware import SwitchHardware


class SwitchStatus(SwitchHardware):

    def __init__(self, gpio_pin):
        # Inherite from SwitchHardware
        SwitchHardware.__init__(self)
        
        # logging configuration
        self.__logger = logging.getLogger(__name__)
        self.__logger.info("Creating new LED instance at GPIO pin '%s'" % str(gpio_pin))
        
        # GPIO setup
        self.__pin = gpio_pin
        GPIO.setup(self.__pin, GPIO.OUT)


    @property
    def on(self):
        return GPIO.input(self.__pin)


    def turn_on(self):
        self.__logger.info("Turning on led")
        GPIO.output(self.__pin, GPIO.HIGH)


    def turn_off(self):
        self.__logger.info("Turning off led")
        GPIO.output(self.__pin, GPIO.LOW)


    def toggle(self):
        self.__logger.info("Toggling led")
        if self.on == False:
            self.on()
        else:
            self.off()


    def __del__(self):
        GPIO.cleanup()
        self.__logger.info("GPIO.cleanup() complete.")

