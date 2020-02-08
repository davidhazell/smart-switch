import logging
import logging.config
import threading
import os, sys
import time
from hue.connection import HueConnection
from switch.switch import Switch


class Main(threading.Thread):

    def __init__(self, hue_bridge_host):
        threading.Thread.__init__(self)

        sys.path.append('..')
        logging.config.fileConfig('config/logging.config')
        self.logger = logging.getLogger(__name__)
        self.logger.info('TEST')

        self.hue    = HueConnection(hue_bridge_host)
        self.switch = Switch()
        self.run()

    def run(self):
        logging.info('Program start')

        while True:
            self.logger.debug(self.hue.room.any_on)
            time.sleep(.025)


if __name__ == "__main__":
    main = Main('192.168.1.37')
