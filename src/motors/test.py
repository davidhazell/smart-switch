from devices import *
import time

led1  = LED(16)
led2  = LED(36)
motor = Motor([7,11,13,15])
#rotary = RotaryEncoder(clk=12,dt=18)

led2.on()

clk = 12
dt  = 18
sw  = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)
swLastState  = GPIO.input(sw)
#GPIO.add_event_detect(sw, GPIO.FALLING, callback=cancel)

try:
        while True:
                clkState = GPIO.input(clk)
                dtState  = GPIO.input(dt)
                swState  = GPIO.input(sw)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                                motor.longstep_forward()
                                led1.toggle()
                                led2.toggle()
                        else:
                                counter -= 1
                                motor.longstep_backward()
                                led1.toggle()
                                led2.toggle()
                        print '[INFO ]  counter: ' + str(counter)
                if swState != swLastState:
                    print "[INFO ] CLICK"
                clkLastState = clkState
                swLastState  = swState
                #time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()


