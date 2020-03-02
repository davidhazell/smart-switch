import logging.config
import time
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from RPi import GPIO
from src.switch.position import SwitchPosition

# Logging
logging.config.fileConfig('../config/logging.config')
logger = logging.getLogger(__name__)

# GPIO
GPIO.setmode()

# Create new SwitchPosition() instance and define update interval
new_switch = SwitchPosition(gpio_clk=23, gpio_dt=24)

update_interval_seconds = 5

# Check switch position every update_interval_seconds
while True:

    if new_switch.power_state == "ON":
        power_state_text="\033[92mON\033[0m"
    else:
        power_state_text="\033[91mOFF\033[0m"

    logger.debug("SWITCH STATE is %s" % power_state_text)
    logger.debug("Checking state again in %s seconds..." % update_interval_seconds)
    time.sleep(update_interval_seconds)

