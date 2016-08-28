#!/usr/bin/env python

import ZeroSeg.led as led
import time

device = led.sevensegment()

while True:
    device.letter(deviceId=0, position=7, char='Z', redraw=False)
    device.letter(deviceId=0, position=6, char='E', redraw=False)
    device.letter(deviceId=0, position=5, char='R', redraw=False)
    device.letter(deviceId=0, position=4, char='O', redraw=False)
    device.letter(deviceId=0, position=3, char='S', redraw=False)
    device.letter(deviceId=0, position=2, char='E', redraw=False)
    device.letter(deviceId=0, position=1, char='G', redraw=False)
    for _ in range(500):
	device.rotate_left()
	time.sleep(0.3)