import ZeroSeg.led as led
import time

device = led.sevensegment(cascaded=2)

device.write_text(1,"YES")

time.sleep(3)

device.clear()
