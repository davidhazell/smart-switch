import logging
import RPi.GPIO as GPIO


class SwitchIndicator:

    def __init__(self, gpio_pin):
        logging.info("Creating new LED instance at GPIO pin '%i'" % int(gpio_pin))
        
        # GPIO setup
        self.__pin = int(gpio_pin)
        GPIO.setup(self.__pin, GPIO.OUT)

    @property
    def on(self):
        return GPIO.input(self.__pin)

    def turn_on(self):
        logging.info("Turning on led at GPIO %s" % self.__pin)
        GPIO.output(self.__pin, GPIO.HIGH)

    def turn_off(self):
        logging.info("Turning off led at GPIO %s" % self.__pin)
        GPIO.output(self.__pin, GPIO.LOW)

    def toggle(self):
        if self.on:
            self.turn_off()
        else:
            self.turn_on()

    def __del__(self):
        self.turn_off()
