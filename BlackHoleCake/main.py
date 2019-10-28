# CircuitPlaygroundExpress_NeoPixel

import time

import board
import neopixel
import math


#pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels = neopixel.NeoPixel(board.A1, 120, brightness=.9)
pixels.fill((0, 0, 0))
pixels.show()



n_pixels = len(pixels)

factors = []

incr_size = 2 * math.pi/n_pixels
for i in range(n_pixels):
    val = (math.sin((i* incr_size)) + 1) / 2.0
    factors.append(val)
    
print(factors)

def scale_factor(i, offset):
    #print(offset)
    index = i + offset
    if index>=n_pixels:
        index = index - n_pixels
    return factors[index]
    
print(scale_factor(30, 0))
print(scale_factor(30, 10))
print(scale_factor(30, 20))
print(scale_factor(30, 30))
print(scale_factor(30, 40))
print(scale_factor(30, 50))
print(scale_factor(30, 60))
print(scale_factor(30, 70))
print(scale_factor(30, 80))
print(scale_factor(30, 90))
print(scale_factor(30, 100))
print(scale_factor(30, 110))
print(scale_factor(30, 120))
print(scale_factor(30, 200))
def black_hole(wait):
    
    n_pixels = len(pixels)
    
    for j in range(255):
        orange_r = 255
        orange_g = 85
        orange_b = 0
        

        for i in range(n_pixels):
            scale = scale_factor(i, j)
            scale_r = int(orange_r * scale)
            scale_g = int(orange_g * scale)
            scale_b = int(orange_b * scale)
            pixels[i] = (scale_r, scale_g, scale_b)
            if i==30:
                print(scale)
            
        pixels.show()
        time.sleep(wait)
        
while True:
    print("Black hole")
    
    black_hole(.001)