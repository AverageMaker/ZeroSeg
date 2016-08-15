#!/usr/bin/env python

import ZeroSeg.led as led
import time

device = led.sevensegment(cascaded=2)

while True:
    device.write_number(deviceId=0, value=1234)
    for x in xrange(2):
        for _ in xrange(8):
            device.scroll_right()
            time.sleep(0.1)
        time.sleep(1)
    device.clear()