import logging
from RPi import GPIO


class SwitchHardware:

    def __init__(self, gpio_mode=GPIO.BOARD):
        # Define logger
        self._logger = logging.getLogger(__name__)
        
        # Configure GPIO
        self._logger.info('Setting GPIO mode=%s' % str(gpio_mode))
        GPIO.setmode(gpio_mode)

    def __del__(self):
        self._logger = logging.getLogger(__name__)

