import logging
import logging.config
import threading
import os, sys
import time
from hue.connection import HueService
from switch.switch import SwitchService


class SmartSwitch(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

        # Logging
        sys.path.append('..')
        logging.config.fileConfig('config/logging.config')
        self.logger = logging.getLogger(__name__)
        self.logger.info('TEST')

        # Services
        self.__hue = HueService()
        self.__switch = SwitchService()


    def run(self):
        logging.info('Program start')

        while True:
            self.logger.debug('LOG')
            time.sleep(5)


if __name__ == "__main__":
    main = SmartSwitch()
