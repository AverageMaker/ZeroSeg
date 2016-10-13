#!/usr/bin/env python

import ZeroSeg.led as led
import time
import random
from datetime import datetime

def date(device, deviceId):

    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year - 2000

    dt = "%02d-%02d-%02d" % (day, month, year)
    device.write_text(deviceId, dt)

device = led.sevensegment()

while True:
    date(device, 0)
    time.sleep(900) #Update every 15 minutes
    device.clear()