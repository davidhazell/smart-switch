import time
from position import SwitchPosition

interval_seconds = 5
new_switch = SwitchPosition()

print "DEBUG: Begin checking switch state"

while True:

    print "DEBUG: SWITCH STATE is %s" % new_switch.power_state
    print "DEBUG: Checking state again in %s seconds..." % interval_seconds
    time.sleep(interval_seconds)



