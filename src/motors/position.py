import logging
import threading
from RPi import GPIO
from time import sleep


class SwitchPosition:

    def __init__(self, clk=17, dt=18):

        # Logging
        self.__logger = logging.getLogger(__name__)
        self.__logger.debug("Creating new SwitchPosition instance with clk=%i and dt=%i" % (clk, dt))

        # Set GPIO board values and initialize
        self.__clk = int(clk)
        self.__dt  = int(dt)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.__dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.__clkLastState = GPIO.input(self.__clk)

        # Initialize counter variable
        # - For now assume switch start position is 0 (middle)
        # - In the future we will use motors to establish start position
        #
        self.__step_counter = 0
        self.__update_interval = 0.01
        
        # Begin monitoring position
        self.__thread = threading.Thread(target=self.__watch_position)
        self.__thread.setDaemon(True)
        self.__thread.start()


    @property
    def power_state(self):
        if self.__step_counter > 0:
            return "ON"
        else:
            return "OFF"


    @property
    def position(self):
        return self.__step_counter


    # Check and update position on a defined interval
    def __watch_position(self):

        while True:
            # Get current GPIO input states
            clkState = GPIO.input(self.__clk)
            dtState = GPIO.input(self.__dt)
            # Compare current state with last state to determine change in position
            if clkState != self.__clkLastState:
                if dtState != clkState:
                    self.__step_counter -= 1
                else:
                    self.__step_counter += 1
                
                self.__logger.debug("Position: %s" % self.__step_counter)

                # Reset clkLastState to current clkState for future comparisons
                self.__clkLastState = clkState
                    
                # Sleep for 1/10 of a second
                sleep(self.__interval)
