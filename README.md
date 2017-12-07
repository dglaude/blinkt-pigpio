# blinkt-pigpio
Blinkt! library that use pigpio rather than RPi.GPIO

*Initial version*
It was a quick and dirty adaptation of the Blinkt! library from Pimoroni https://github.com/pimoroni/blinkt
Most copyright goes to Pimoroni that released under MIT.

Rather than to use RPi.GPIO to drive GPIO of the local Pi, it use pigpio to do the same thing, but bit banging on remote GPIO is not optimal.

That version is still available as blinkt_bitbang.py but should be avoided.

*Second version*
Thi use the wave function from pigpio.
It is based on the Pyhon APA102 example code found here:
http://abyz.me.uk/rpi/pigpio/examples.html#Python code

Copyright goes to Pimoroni for the Blinkt! API and base code.
And pigpio exemple is Public Domain
# APA102 LED strip driver
# 2017-03-28

This version is a single file 'blinkt.py' to put next to a Blinkt! example.

You can find more information about pigpio here: http://abyz.me.uk/rpi/pigpio/index.html

Basically, you need to have pigpiod running on the Pi where you have the Blinkt! attached. Then you need to configure the proper environment variable to tell wich IP to use to communicate with that Pi from where you run the Blink! example.

export PIGPIO_ADDR=10.0.99.1

This become particularly interesting if you use a PiZero and remote GPIO pin as with the usbbootgui from Raspbian Desktop (x86) or with Pirate Python.

You can acquire the Blinkt! from here: https://shop.pimoroni.com/products/blinkt

Eight super-bright RGB LED indicators, ideal for adding visual notifications to your Raspberry Pi on their own or on a pHAT stacking header.

