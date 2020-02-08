from RPi import GPIO
from time import sleep
import threading

class SwitchPosition:

    def __init__(self, clk=17, dt=18, gpio_mode="GPIO.BCM"):

        # Set GPIO board values and initialize
        self.__clk = str(clk)
        self.__dt  = str(dt)
        GPIO.setmode(gpio_mode)
        GPIO.setup(self.__clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.__dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.__clkLastState = GPIO.input(self.__clk)

        # Initialize counter variable
        #
        # * For now assume switch start position is 0 (middle)
        # * In the future we will use motors to establish start position
        #
        self.__counter = 0
        
        # Begin monitoring position
        self.__thread = threading.Thread(target=self.__watch_position)
        self.__thread.setDaemon(True)
        self.__thread.start()
        self.transitiontime(0)


    @property
    def power_state(self):
        if self.__counter > 0:
            return True
        else:
            return False


    @property
    def position(self):
        return self.__counter


    def __watch_position(self):
        try:

            while True:
                # Get current GPIO input states
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                # Compare current state with last state to determine change in position
                if clkState != self.__clkLastState:
                    if dtState != clkState:
                        self.__counter += 1
                    else:
                        self.__counter -= 1
                    
                    print "DEBUG: position=%i" % self.__counter
                 
                    # Reset clkLastState to current clkState for future comparisons
                    self.__clkLastState = clkState
                    
                    # Sleep for 1/10 of a second
                    sleep(0.01)
        finally:
            GPIO.cleanup()

