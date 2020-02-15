import time
import sys
import logging, logging.config
sys.path.append('..')
from src.motors.position import SwitchPosition


# Logging
logging.config.fileConfig('../config/logging.config')
logger = logging.getLogger(__name__)

# Create new SwitchPosition() instance and define update interval
new_switch = SwitchPosition()
update_interval_seconds = 5

logger.debug("Begin checking switch state")

# Check switch position every update_interval_seconds
while True:

    if new_switch.power_state == "ON":
        power_state_text="\033[92mON\033[0m"
    else:
        power_state_text="\033[91mOFF\033[0m"

    logger.debug("SWITCH STATE is %s" % power_state_text)
    logger.debug("Checking state again in %s seconds..." % update_interval_seconds)
    time.sleep(update_interval_seconds)



