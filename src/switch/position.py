import logging
import threading
from RPi import GPIO
from time import sleep


class SwitchPosition:

    def __init__(self, gpio_clk, gpio_dt):

        # Logging
        logging.getLogger(__name__)
        logging.debug("Creating new SwitchPosition instance at GPIO pins \'%i\' and \'%i\'" % (int(gpio_clk),
                                                                                               int(gpio_dt)))

        # Set GPIO board values and initialize
        self.__clk = int(gpio_clk)
        self.__dt = int(gpio_dt)
        GPIO.setup(self.__clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.__dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.__clkLastState = GPIO.input(self.__clk)

        # Initialize counter variable and interval at which to check position
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
    def on(self):
        if self.__step_counter > 0:
            return True
        else:
            return False

    @property
    def position(self):
        return self.__step_counter

    # Check and update position on a defined interval
    def __watch_position(self):

        logging.info('Starting thread to monitor switch position')

        while True:
            # Get current GPIO input states
            clkState = GPIO.input(self.__clk)
            dtState = GPIO.input(self.__dt)
            # Compare current state with last state to determine change in position
            if clkState != self.__clkLastState:
                if dtState != clkState:
                    self.__step_counter += 1
                    logging.debug("Position changed: %s (+1)" % self.__step_counter)
                else:
                    self.__step_counter -= 1
                    logging.debug("Position changed: %s (-1)" % self.__step_counter)

                # Reset clkLastState to current clkState for future comparisons
                self.__clkLastState = clkState

                # Sleep for 1/10 of a second
                # sleep(self.__update_interval)
