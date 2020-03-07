import logging
import time
import RPi.GPIO as GPIO


class SwitchMovement:

    def __init__(self, gpio_pin):

        # Logging configuration
        logging.getLogger(__name__)
        logging.info("Creating new motor instance at GPIO pin '%i'" % int(gpio_pin))

        # ToDo: GPIO setup
        self.__pin = int(gpio_pin)
        GPIO.setup(self.__pin, GPIO.OUT)
        self.__pwm = GPIO.PWM(self.__pin, 100)
        self.__motor_power_interval = 1

    def activate(self):
        logging.info('Activating motor at GPIO %i' % self.__pin)
        self.__pwm.start(100)

        GPIO.output(self.__pin, GPIO.HIGH)
        #time.sleep(self.__motor_power_interval)
        GPIO.output(self.__pin, GPIO.LOW)

        self.__pwm.stop()

    def __del__(self):
        pass