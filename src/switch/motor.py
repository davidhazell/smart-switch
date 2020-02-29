from RPi import GPIO
from hardware import SwitchHardware
import time


class SwitchMovement(SwitchHardware):

    def __init__(self, pin):
        # Inherit from SwitchHardware
        SwitchHardware.__init__(self)

        # Logging configuration
        self.__logger = loggingConfig.getLogger(__name__)

        # ToDo: GPIO setup
        self.__pin = pin
        GPIO.setup(self.__pin, GPIO.LOW)
        self.__motor_power_interval = .001

    def activate(self):
        GPIO.output(self.__pin, GPIO.HIGH)
        time.sleep(self.__motor_power_interval)
        GPIO.output(self.__pin, GPIO.LOW)

