from RPi import GPIO
from time import sleep
import threading

class SwitchPosition:

    def __init__(self, clk=17, dt=18):

        print "DEBUG: BEGIN SwitchPosition.__init__()"

        # Set GPIO board values and initialize
        self.__clk = int(clk)
        self.__dt  = int(dt)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.__dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.__clkLastState = GPIO.input(self.__clk)

        # Initialize counter variable
        #
        # * For now assume switch start position is 0 (middle)
        # * In the future we will use motors to establish start position
        #
        self.__counter = 0
        self.__interval = 0.01
        
        # Begin monitoring position
        print "DEBUG: BEFORE threading.Thread()"
        self.__thread = threading.Thread(target=self.__watch_position)
        print "DEBUG: BEFORE setDaemon()"
        self.__thread.setDaemon(True)
        print "DEBUG: BEFORE start()"
        self.__thread.start()
        print "DEBUG: END SwitchPosition.__INIT__()"


    @property
    def power_state(self):
        if self.__counter > 0:
            return "ON"
        else:
            return "OFF"


    @property
    def position(self):
        return self.__counter


    def __watch_position(self):

        print "DEBUG: SwitchPosition.__watch_position()"

        while True:
            # Get current GPIO input states
            clkState = GPIO.input(self.__clk)
            dtState = GPIO.input(self.__dt)
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
                sleep(self.__interval)

