from position import SwitchPosition

class SwitchService:

    def __init__(self):

        # Logging
        self.__logger = logging.getLogger(__name__)
        self.__logger.debug("Creating new Switch instance")

        # Create position and motor instances
        self.__position   = SwitchPosition(clk=17, dt=18)
        self.__motor_up   = SwitchMotor()
        self.__motor_down = SwitchMotor()

        # Setup queue connection


    @property
    def position(self)
        return self.__position.state

