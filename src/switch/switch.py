from rotaryencoder import SwitchPosition
from motor import SwitchMotion
from led import SwitchStatus

class SwitchService:

    def __init__(self):

        # Logging
        self.__logger = logging.getLogger(__name__)
        self.__logger.debug("Creating new Switch instance")

        # Create hardware instances
        # ToDo: Get values from application.properties
        self.__position   = SwitchPosition(clk=17, dt=18)
        self.__motor_up   = SwitchMotion()
        self.__motor_down = SwitchMotion()
        self.__led_good   = SwitchStatus()
        self.__led_bad    = SwitchStatus()


    # Get current position of switch
    @property
    def get_switch_state(self):
        return self.__position.on


    # Activate motor to move switch to 'on' position
    def move_switch_up(self):
        return self.__motor_up.activate()

    
    # Activate motor to move switch to 'off' position
    def move_switch_down(self):
        return self.__motor_down.activate()


    def set_led_good(self):
        self.__led_good.on()
        self.__led_bad.off()


    def set_led_bad(self):
        self.__led_good.off()
        self.__led_bad.on()


    def __del__(self):
        GPIO.cleanup()
        self.__logger.info('GPIO.cleanup() complete.)

