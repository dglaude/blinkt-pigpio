# blinkt-pigpio
Blinkt! library that use pigpio rather than RPi.GPIO

This is a quick and dirty adaptation of the Blinkt! library from Pimoroni
https://github.com/pimoroni/blinkt

Most copyright goes to them (only a few minor change from David Glaude).
Replaced line of code have a ### in front.

It is a single file 'blinkt.py' that you can put next to a working Blinkt! example.

Rather than to use RPi.GPIO to drive GPIO of the local Pi...
It use pigpio to do the same thing.
You can find pigpio here: http://abyz.me.uk/rpi/pigpio/index.html
In particular the Python API: http://abyz.me.uk/rpi/pigpio/python.html

Currently this is the worst possible implementation that use GPIO bit banging.

Search APA102 example on this page: http://abyz.me.uk/rpi/pigpio/examples.html#Python code

APA102 LED strip driver
2017-03-28
Script to drive an APA102 LED strip. Three different methods are demonstrated - using spidev SPI (only works on the local Pi), pigpio SPI, and pigpio waves. The SPI solutions only work with the dedicated SPI GPIO. Waves may use any spare GPIO. Four different examples are given including a LED strip clock.

However pigpio also work over the network if you set properly the environmental variable.

This become particularly interesting if you use a PiZero and remote GPIO pin as with the usbbootgui from Raspbian Desktop (x86).

You can acquire the Blinkt! from here: https://shop.pimoroni.com/products/blinkt

Eight super-bright RGB LED indicators, ideal for adding visual notifications to your Raspberry Pi on their own or on a pHAT stacking header.

