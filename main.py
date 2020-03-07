import configparser
import logging.config
import threading
import time
import sys
import RPi.GPIO as GPIO

from src.lights.connection import HueConnection
from src.switch.switch import SwitchService


class SmartSwitch(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

        # Properties
        config = configparser.ConfigParser()
        config.read("config/application.ini")

        # Logging
        logging.config.fileConfig(config["logging"]["logging.config"])
        logging.getLogger(__name__)
        logging.getLogger().setLevel(config["logging"]["logging.level"])

        # Services
        #self.__hue = HueConnection(host    = config["lights"]["host"],
        #                           api_key = config["lights"]["api_key"],
        #                           room    = config["lights"]["room"])

        self.__switch = SwitchService(gpio_mode       = config["switch"]["gpio.mode"],
                                      position_clk    = config["switch"]["rotaryencoder.clk"],
                                      position_dt     = config["switch"]["rotaryencoder.dt"],
                                      motor_on_pin    = config["switch"]["motor.on.pin"],
                                      motor_off_pin   = config["switch"]["motor.off.pin"],
                                      led_success_pin = config["switch"]["led.success.pin"],
                                      led_neutral_pin = config["switch"]["led.neutral.pin"],
                                      led_failure_pin = config["switch"]["led.failure.pin"],)

    def run(self):
        logging.info("Program start")

        last_position = self.__switch.position.position

        while True:
            if last_position != self.__switch.position.position:
                if self.__switch.position.position > 0:
                    self.__switch.led_failure.turn_off()
                    self.__switch.led_neutral.turn_off()
                    self.__switch.led_success.turn_on()
                elif self.__switch.position.position < 0:
                    self.__switch.led_success.turn_off()
                    self.__switch.led_neutral.turn_off()
                    self.__switch.led_failure.turn_on()
                else:
                    self.__switch.led_success.turn_off()
                    self.__switch.led_failure.turn_off()
                    self.__switch.led_neutral.turn_on()
                last_position = self.__switch.position.position


if __name__ == "__main__":
    try:
        main = SmartSwitch()
        main.start()
    except KeyboardInterrupt:
        print('Interrupted')
        GPIO.cleanup()
        sys.exit(0)
