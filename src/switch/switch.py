import logging
import logging.config
import sys
from RPi import GPIO

from src.switch.position import SwitchPosition
from src.switch.motor import SwitchMovement
from src.switch.led import SwitchIndicator


class SwitchService:

    def __init__(self, gpio_mode, position_clk, position_dt, motor_on_pin, motor_off_pin,
                 led_success_pin, led_failure_pin):

        # Logging
        self.__logger = logging.getLogger(__name__)
        self.__logger.debug("Creating new Switch instance")

        if gpio_mode == "BOARD":
            GPIO.setmode(GPIO.BOARD)
        elif gpio_mode == "BCM":
            GPIO.setmode(GPIO.BCM)
        else:
            self.__logger.fatal("Invalid GPIO mode \'%s\'" % gpio_mode)
            sys.exit(1)

        # Create hardware instances
        # ToDo: Get values from application.ini
        self.__position    = SwitchPosition(gpio_clk=position_clk, gpio_dt=position_dt)
        self.__motor_on    = SwitchMovement(motor_on_pin)
        self.__motor_off   = SwitchMovement(motor_off_pin)
        self.__led_success = SwitchIndicator(led_success_pin)
        self.__led_failure = SwitchIndicator(led_failure_pin)

    # Get current position of switch
    @property
    def get_switch_state(self):
        return self.__position.on

    # Activate motor to move switch to 'on' position
    def move_switch_up(self):
        return self.__motor_on.activate()

    # Activate motor to move switch to 'off' position
    def move_switch_down(self):
        return self.__motor_off.activate()

    def set_status_good(self):
        self.__led_success.turn_off()
        self.__led_success.turn_on()

    def set_status_bad(self):
        self.__led_success.turn_off()
        self.__led_falure.turn_on()

    def __del__(self):
        GPIO.cleanup()
