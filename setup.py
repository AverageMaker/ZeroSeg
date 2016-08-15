#!/usr/bin/env python

from distutils.core import setup,Extension
setup(
    name = "ZeroSeg",
    version = "0.0.1",
    author = "Richard Saville",
    author_email = "averagemanvspi@gmail.com",
    description = ("Code library for the ZeroSeg 7-segment display add-on board for the Raspberry Pi Zero"),
    license = "MIT",
    keywords = "raspberry pi rpi led max7219 matrix seven segment zeroseg",
    url = "https://github.com/AverageManVsPi/ZeroSeg",
    packages=['ZeroSeg'],
)
