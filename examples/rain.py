from __future__ import division
import time
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
PIXEL_COUNT = 159
PIXEL_CLOCK = 18
PIXEL_DOUT  = 23
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)
pixels.clear()
pixels.show()
RED=[0]*159
BLUE=[0]*159
GREEN=[0]*159
while True:
	rgb = [255,0,0]
	decColor = 0
	for decColor in range(0,3):
		incColor = 0 if decColor==2 else decColor+1
	i = 0
	for i in range(0,5):
		rgb[decColor] -= 50
		rgb[incColor] += 50
		
		RED[0] = rgb[0]
		GREEN[0] = rgb[1]
		BLUE[0] = rgb[2]
		pixels.set_pixel_rgb(0,RED[0],GREEN[0],BLUE[0])
		pixels.show()
		time.sleep(0.0001)
		c = 159
		for c in range (159,0):
			RED[c] = RED[c-1]
			GREEN[c] = GREEN[c-1]
			BLUE[c] = BLUE[c-1]