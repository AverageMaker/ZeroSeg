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

    # Set day
    device.letter(deviceId, 8, int(day / 10))     # Tens
    device.letter(deviceId, 7, day % 10)          # Ones
    device.letter(deviceId, 6, '-')               # dash
    # Set day
    device.letter(deviceId, 5, int(month / 10))     # Tens
    device.letter(deviceId, 4, month % 10)     # Ones
    device.letter(deviceId, 3, '-')               # dash
    # Set day
    device.letter(deviceId, 2, int(year / 10))     # Tens
    device.letter(deviceId, 1, year % 10)     # Ones

def clock(device, deviceId, seconds):

    for _ in xrange(seconds):
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        dot = second % 2 == 0                # calculate blinking dot
        # Set hours
        device.letter(deviceId, 4, int(hour / 10))     # Tens
        device.letter(deviceId, 3, hour % 10, dot)     # Ones
        # Set minutes
        device.letter(deviceId, 2, int(minute / 10))   # Tens
        device.letter(deviceId, 1, minute % 10)        # Ones
        time.sleep(1)

device = led.sevensegment(cascaded=2)

while True:
    date(device, 1)
    time.sleep(5)
    device.clear()
    clock(device, 1, seconds=5)
    device.clear()
