import logging
import logging.config
import inspect
import sys
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this "
          "by using 'sudo' to run your script")

from src.switch.position import SwitchPosition
from src.switch.motor import SwitchMovement
from src.switch.led import SwitchIndicator


class SwitchService:

    def __init__(self, gpio_mode, position_clk, position_dt, motor_on_pin, motor_off_pin,
                 led_success_pin, led_neutral_pin, led_failure_pin):

        # Logging
        logging.getLogger(__name__)
        logging.debug("Creating new Switch instance")

        #signature = inspect.signature(SwitchService.__init__)
        #for name, parameter in signature.items():
        #    self.__logger.debug(name, parameter.default, parameter.annotation, parameter.kind)

        # Set GPIO mode
        if gpio_mode == "BOARD":
            GPIO.setmode(GPIO.BOARD)
        elif gpio_mode == "BCM":
            GPIO.setmode(GPIO.BCM)
        else:
            logging.critical("Invalid GPIO mode \'%s\'" % gpio_mode)
            sys.exit(1)

        logging.debug("GPIO mode is %s" % GPIO.getmode())

        # Create hardware instances
        # Get values from application.ini
        self.__position    = SwitchPosition(gpio_clk=position_clk, gpio_dt=position_dt)
        self.__motor_on    = SwitchMovement(motor_on_pin)
        self.__motor_off   = SwitchMovement(motor_off_pin)
        self.__led_success = SwitchIndicator(led_success_pin)
        self.__led_neutral = SwitchIndicator(led_neutral_pin)
        self.__led_failure = SwitchIndicator(led_failure_pin)

    # Get current position of switch
    @property
    def get_switch_state(self):
        return self.__position.on

    @property
    def position(self):
        return self.__position

    @property
    def led_success(self):
        return self.__led_success

    @property
    def led_neutral(self):
        return self.__led_neutral

    @property
    def led_failure(self):
        return self.__led_failure

    @property
    def motor_on(self):
        return self.__motor_on

    @property
    def motor_off(self):
        return self.__motor_off

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
        self.__led_failure.turn_on()

    def __del__(self):
        # Clear GPIO configurations
        GPIO.cleanup()
