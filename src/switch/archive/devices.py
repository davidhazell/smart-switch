import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


class Motor:

    HALFSTEP_SEQ = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
    ]

    def __init__(self, control_pins):
        
        # Setup pins
        self.control_pins = control_pins
        for pin in control_pins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,0)

        # Set step
        self.current_step = 0

    @property
    def state(self):
        return self.HALFSTEP_SEQ[self.current_step]

    def longstep_forward(self):
        for i in range(100):
            print '[TRACE] longstep_forward(%d)' % i
            self.halfstep_forward()

    def longstep_backward(self):
        for i in range(100):
            print '[TRACE] longstep_forward(%d)' % i
            self.halfstep_backward()

    def step_forward(self):
        if self.current_step == len(self.HALFSTEP_SEQ) - 2:
            self.current_step = 0
            self.set_pins(self.current_step)
        else:
            self.current_step += 2
            self.set_pins(self.current_step)

    def step_backward(self):
        if self.current_step == 0:
            self.current_step = len(self.HALFSTEP_SEQ) -2
            self.set_pins(self.current_step)
        else:
            self.current_step -= 2
            self.set_pins(self.current_step)

    def halfstep_forward(self):
        if self.current_step == len(self.HALFSTEP_SEQ) - 1:
            self.current_step = 0
            self.set_pins(self.current_step)
        else:
            self.current_step += 1
            self.set_pins(self.current_step)

    def halfstep_backward(self):
        if self.current_step == 0:
            self.current_step = len(self.HALFSTEP_SEQ) - 1
            self.set_pins(self.current_step)
        else:
            self.current_step -= 1
            self.set_pins(self.current_step)

    def set_pins(self, halfstep):
        for pin in range(4):
            GPIO.output(self.control_pins[pin], self.HALFSTEP_SEQ[halfstep][pin])

    def __del__(self):
        GPIO.cleanup()


class RotaryEncoder:

    def __init__(self, clk, dt):

        self.clk = clk
        self.dt  = dt

        GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(dt,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.counter = 0
        self.clkLastState = GPIO.input(clk)

    def __init__(self):
        GPIO.cleanup()


class LED:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    @property
    def state(self):
        return GPIO.input(self.pin)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def toggle(self):
        if self.state == 0:
            self.on()
        else:
            self.off()

    def __del__(self):
        GPIO.cleanup()

'''
led    = LED(16)
#rotary = RotaryEncoder(clk=, dt=)
motor  = Motor([7,11,13,15])

for i in range(10000):
    print motor.state
    motor.step_forward()
    time.sleep(.0001)
'''
