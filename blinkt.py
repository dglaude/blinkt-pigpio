# This is a mix between

# pigpio APA102 python example:
# 2017-03-28
# Public Domain

# Blinkt! library under MIT License
# Copyright (c) 2017 Pimoroni Ltd.
# See LICENSE

import atexit
import pigpio

__version__ = '0.0.1'

pi = pigpio.pi()

DAT = 23
CLK = 24

DATB=(1<<DAT)
CLKB=(1<<CLK)

NUM_PIXELS = 8
BRIGHTNESS = 7

pixels = [[0, 0, 0, BRIGHTNESS]] * NUM_PIXELS

apa102_cmd=[0]*4 + [0xe1,0, 0, 0]*NUM_PIXELS + [255]*4
chain=[None]*(2*len(apa102_cmd))
gwid=[None]*16

def create_byte_waves():
   for i in range(16):
      pulse=[]
      for bit in range(4):
         if (1<<(3-bit)) & i: # 1 bit
            pulse.append(pigpio.pulse(DATB, CLKB, 1))
         else: # 0 bit
            pulse.append(pigpio.pulse(0, DATB|CLKB, 1))
         pulse.append(pigpio.pulse(CLKB, 0, 1))
      pi.wave_add_generic(pulse)
      gwid[i] = pi.wave_create()

pi = pigpio.pi()
if not pi.connected:
   exit()
create_byte_waves()

_gpio_setup = False
_clear_on_exit = True

def _exit():
    if _clear_on_exit:
        clear()
        show()

    while pi.wave_tx_busy():
        pass
    for w in gwid:
        pi.wave_delete(w)
    pi.set_mode(DAT, oldDATmode)
    pi.set_mode(CLK, oldCLKmode)
    pi.stop()

def set_brightness(brightness):
    """Set the brightness of all pixels

    :param brightness: Brightness: 0.0 to 1.0
    """

    if brightness < 0 or brightness > 1:
        raise ValueError("Brightness should be between 0.0 and 1.0")

    for x in range(NUM_PIXELS):
        pixels[x][3] = int(31.0 * brightness) & 0b11111

def clear():
    """Clear the pixel buffer"""
    for x in range(NUM_PIXELS):
        pixels[x][0:3] = [0, 0, 0]

def tx_bytes(bytes):
   global chain
   while pi.wave_tx_busy():
      pass
   j = 0
   for i in range(len(bytes)):
      chain[j] = gwid[(bytes[i]>>4)&15]
      j += 1
      chain[j] = gwid[bytes[i]&15]
      j += 1
   pi.wave_chain(chain)

def show():
    """Output the buffer to Blinkt!

    This is using pigpio wave technique.
    """
    global _gpio_setup

    if not _gpio_setup:
        oldDATmode = pi.get_mode(DAT)
        oldCLKmode = pi.get_mode(CLK)
        pi.set_mode(DAT, pigpio.OUTPUT)
        pi.set_mode(CLK, pigpio.OUTPUT)
        _gpio_setup = True

    tx_bytes(apa102_cmd)


# TODO: verify that this is working on small dark die APA102s
# Emit exactly enough clock pulses to latch the small dark die APA102s which are weird
# for some reason it takes 36 clocks, the other IC takes just 4 (number of pixels/2)


def set_all(r, g, b, brightness=None):
    """Set the RGB value and optionally brightness of all pixels

    If you don't supply a brightness value, the last value set for each pixel be kept.

    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """
    for x in range(NUM_PIXELS):
        set_pixel(x, r, g, b, brightness)

def get_pixel(x):
    """Get the RGB and brightness value of a specific pixel"""

    r, g, b, brightness = pixels[x]
    brightness /= 31.0

    return r, g, b, round(brightness, 3)

def set_pixel(x, r, g, b, brightness=None):
    """Set the RGB value, and optionally brightness, of a single pixel

    If you don't supply a brightness value, the last value will be kept.

    :param x: The horizontal position of the pixel: 0 to 7
    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """
#def set_LED_RGB(led, r, g, b):
    offset = (x*4) +4
    apa102_cmd[offset+1] = b
    apa102_cmd[offset+2] = g
    apa102_cmd[offset+3] = r

    if brightness is None:
        brightness = pixels[x][3]
    else:
        brightness = int(31.0 * brightness) & 0b11111
#def set_LED_PRGB(led, p, r, g, b):
        apa102_cmd[offset  ] = 0xE0 + brightness 

    pixels[x] = [int(r) & 0xff, int(g) & 0xff, int(b) & 0xff, brightness]



def set_clear_on_exit(value=True):
    """Set whether Blinkt! should be cleared upon exit

    By default Blinkt! will turn off the pixels on exit, but calling::

        blinkt.set_clear_on_exit(False)

    Will ensure that it does not.

    :param value: True or False (default True)
    """
    global _clear_on_exit
    _clear_on_exit = value


