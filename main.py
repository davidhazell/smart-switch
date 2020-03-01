import configparser
import logging.config
import threading
import time

from src.lights.connection import HueConnection
from src.switch.switch import SwitchService


class SmartSwitch(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

        # Logging
        logging.config.fileConfig("config/logging.config")
        self.logger = logging.getLogger(__name__)

        # Properties
        config = configparser.ConfigParser()
        config.read("config/application.ini")

        # Services
        #self.__hue = HueConnection(host    = config["lights"]["host"],
        #                           api_key = config["lights"]["api_key"],
        #                           room    = config["lights"]["room"])

        self.__switch = SwitchService(gpio_mode     = config["switch"]["gpio.mode"],
                                      position_clk  = config["switch"]["rotaryencoder.clk"],
                                      position_dt   = config["switch"]["rotaryencoder.dt"],
                                      motor_on_pin  = config["switch"]["motor.on.pin"],
                                      motor_off_pin = config["switch"]["motor.off.pin"],
                                      led_success   = config["switch"]["led.success.pin"],
                                      led_failure   = config["switch"]["led.failure.pin"],)

    def run(self):
        logging.info("Program start")

        while True:
            self.logger.debug('LOG')
            time.sleep(5)


if __name__ == "__main__":
    main = SmartSwitch()
