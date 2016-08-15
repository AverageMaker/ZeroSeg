ZeroSeg 
==============

A code library for the ZeroSeg Raspberry Pi Zero add-on board from [[ThePiHut.com.](#)]

IMAGE

This board is designed and wired in the exact same way as the common 7-segment modules available, allowing the use of existing code and libraries to easily code your projects.

This code library was originally copied from Richard Hull's open source MAX7219 library [[right here on GitHub.](https://github.com/rm-hull/max7219)] 

This library makes it easy to scroll numbers and text along the Skeleseg's twin 7-segment displays, running via the MAX7219 IC, with just a few simple lines of code.

Raspberry Pi Setup & Installation
------------
MODIFY - DO IT CODE STYLE

I recommend using a fresh Raspbian image to avoid any conflicts.

 1. Download and install the latest copy of Raspbian from here: https://www.raspberrypi.org/downloads/raspbian/
 2. Boot (power on) your Raspberry Pi. The displays may light up, this is perfectly normal.
 3. In a terminal window, update Raspbian using ***sudo apt-get update*** and then ***sudo apt-get upgrade***.
 4. Next run ***sudo raspi-config*** and enable SPI. Select option 9 '***Advanced Options***' and then option 5 '***SPI***'. Select ***Yes*** to enable the SPI interface and hit enter.
 5. Exit the config tool by selecting '***Finish'***
 6. Reboot your Raspberry Pi by entering 'sudo reboot' and hit enter
 7. Once rebooted, run ***sudo apt-get install git build-essential python-dev***. Enter 'Y' when prompted, and hit enter. Let the install run.
 8. Enter ***cd*** in the terminal and hit enter, to ensure you're in the home directory
 9. Next run ***git clone https://github.com/AverageManVsPi/ZeroSeg.git*** to download the ZeroSeg code library to your Pi.
 10. Enter ***cd ZeroSeg*** to enter your new ZeroSeg directory
 11. Next run ***sudo python setup.py install***
 12. With the files now downloaded, complete the SPI setup. First go into the library directory by using ***cd ZeroSeg***
 15. Next run ***sudo pip install spidev***
 16. Optional: To delete the files you probably won't need, and reduce clutter, whilst in the ZeroSeg directory run ***rm LICENSE.md***, ***rm README.md*** and ***rm setup.py***.
    
Run Example Code
------------
To make sure everything's working as it should, run the test script.

 1. Enter ***cd*** in the terminal to make sure we're starting from the same place (the home directory)
 2. Now enter ***cd ZeroSeg*** - this will take you to the main ZeroSeg directory
 3. Next enter ***cd examples*** to go to the example script directory
 4. To run the test script, run ***sudo python zeroseg_example.py***
 5. The displays should show the date, then the brightness should fade in and out. The date will then scroll left, followed by the time being displayed. Next the display will count up from a negative number, followed by hex numbers and finally random number count.

*NOTE:* By default, SPI is only accessible by root (hence using `sudo` above). Follow these instructions to create an spi group, and adding your user to that group, so you don't have to
run as root: http://quick2wire.com/non-root-access-to-spi-on-the-pi

Coding Basics
------------
Start your file by importing and initialising the `sevensegment` class:

```python
import max7219.led as led
device = led.sevensegment()
```
You can now start with something simple like displaying a number for 5 seconds on one of the displays. The deviceId is 0 for the right display and 1 for the left display:

```python
import max7219.led as led
import time
device = led.sevensegment()
device.write_number(deviceId=0, value=1234)
time.sleep(5)

```

ADD OTHER EXAMPLES
IP ADDRESS
TIME
DATE
SCROLLING
SCORE ETC
   
GPIO pin-outs
-------------
UPDATE THIS SECTION

| Board Pin | Name | Remarks     | RPi Pin | RPi Function      |
|:----------:|:----:|:-----------:|:-------:|-------------------|
| 1         | VCC  | +5V Power   | 2       | 5V0               |
| 2         | GND  | Ground      | 6       | GND               |
| 3         | DIN  | Data In     | 19      | GPIO 10 (MOSI)    |
| 4         | CS   | Chip Select | 24      | GPIO 8 (SPI CE0)  |
| 5         | CLK  | Clock       | 23      | GPIO 11 (SPI CLK) |


References
----------
UPDATE THIS SECTION

* http://hackaday.com/2013/01/06/hardware-spi-with-python-on-a-raspberry-pi/
* http://gammon.com.au/forum/?id=11516
* http://louisthiery.com/spi-python-hardware-spi-for-raspi/
* http://www.brianhensley.net/2012/07/getting-spi-working-on-raspberry-pi.html
* http://raspi.tv/2013/8-x-8-led-array-driven-by-max7219-on-the-raspberry-pi-via-python
* http://quick2wire.com/non-root-access-to-spi-on-the-pi

License
-------
*This code library is a modified version of Richard Hull's MAX7219 library, therefore the license details, as requested, are being included here:*

The MIT License (MIT)

Copyright (c) 2015 Richard Hull

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
