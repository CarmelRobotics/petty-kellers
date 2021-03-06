
# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
# Will color all the lights different primary colors.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI


# Configure the count of pixels:
PIXEL_COUNT = 159

# The WS2801 library makes use of the BCM pin numbering scheme. See the README.md for details.

# Specify a software SPI connection for Raspberry Pi on the following pins:
PIXEL_CLOCK = 18
PIXEL_DOUT  = 23
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
#SPI_PORT   = 0
#SPI_DEVICE = 0
#pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Clear all the pixels to turn them off.
pixels.clear()
pixels.show()  # Make sure to call show() after changing any pixels!

# Set the first third of the pixels red.
def wheel(pos):
    if pos < 85:
        return Adafruit_WS2801.RGB_to_color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Adafruit_WS2801.RGB_to_color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Adafruit_WS2801.RGB_to_color(0, pos * 3, 255 - pos * 3)

# Define rainbow cycle function to do a cycle of all hues.
def rainbow_cycle(pixels, wait=0):
    for j in range(256): # one cycle of all 256 colors in the wheel
	for i in range(pixels.count()):
            # tricky math! we use each pixel as a fraction of the full 96-color wheel
            # (thats the i / strip.numPixels() part)
            # Then add in j which makes the colors go around per pixel
            # the % 96 is to make the wheel cycle around
            	pixels.set_pixel(i, wheel(((i * 256 // pixels.count()) + j) % 256) )
            	if wait > 0:
                	time.sleep(wait)
	if j%5==0:
		pixels.show()

print('Rainbow cycling, press Ctrl-C to quit...')


team = raw_input('Which Team? ')
while True:
	if team == 'green':	
		for i in range(19):
			pixels.set_pixel_rgb(i, 0, 255, 0)  # Set the RGB color (0-255) of pixel i.
	elif team =='red':
		for i in range(19):
			pixels.set_pixel_rgb(i, 0, 0, 255)  # Set the RGB color (0-255) of pixel i.
	elif team =='rain': 
		rainbow_cycle(pixels)
	elif 1 == 1:
		for i in range(19):
    			pixels.set_pixel_rgb(i, 255, 0, 0)  # Set the RGB color (0-255) of pixel i.






# Now make sure to call show() to update the pixels with the colors set above!
	pixels.show()

# Not used but you can also read pixel colors with the get_pixel_rgb function:
#r, g, b = pixels.get_pixel_rgb(0)  # Read pixel 0 red, green, blue value.


#I'm so sorry...