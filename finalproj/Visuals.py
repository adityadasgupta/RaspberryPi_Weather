from sense_emu import SenseHat
import random
import time

sense = SenseHat()

'''
O = [40, 40, 40]  # BLACK BACKGROUND
X = [170, 170, 170]  # CLOUD GREY
D = [100, 100, 255]  #RAINDROP BLUE

rain_cloud = [
O, O, X, X, X, X, O, O,
O, X, X, X, X, X, X, O,
O, D, X, X, X, X, O, O,
O, O, O, D, O, D, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

rain_cloud_i1 = [
O, O, O, X, X, X, X, O,
O, O, X, X, X, X, X, X,
O, O, O, X, X, X, X, O,
O, D, O, O, O, O, O, O,
O, O, D, O, D, O, D, O,
O, O, O, D, O, D, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

rain_cloud_i2 = [
O, O, X, X, X, X, O, O,
O, X, X, X, X, X, X, O,
O, O, X, X, X, X, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, D, O, O, D, O, O, O,
O, O, D, O, O, D, D, O,
O, O, O, D, O, O, O, O
]

rain_cloud_i3 = [
O, X, X, X, X, O, O, O,
X, X, X, X, X, X, O, O,
O, X, X, X, X, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, D, O, O, D, O, O, O,
O, O, D, O, O, D, O, O
]

while True:
    sense.set_pixels(rain_cloud)
    time.sleep(1)
    sense.set_pixels(rain_cloud_i1)
    time.sleep(1)
    sense.set_pixels(rain_cloud_i2)
    time.sleep(1)
    sense.set_pixels(rain_cloud_i3)
    time.sleep(1)
'''


'''
Y = [253,184,19]
B = [100,100,255]

sun = [
B, B, B, B, Y, B, B, B,
B, Y, B, B, B, B, Y, B,
B, B, B, Y, Y, B, B, B,
Y, B, Y, Y, Y, Y, B, B,
B, B, Y, Y, Y, Y, B, Y,
B, B, B, Y, Y, B, B, B,
B, Y, B, B, B, B, Y, B,
B, B, B, Y, B, B, B, B
]

sun_i1 = [
B, B, B, Y, B, Y, B, B,
B, B, B, B, B, B, B, B,
Y, B, B, Y, Y, B, B, B,
B, B, Y, Y, Y, Y, B, Y,
Y, B, Y, Y, Y, Y, B, B,
B, B, B, Y, Y, B, B, Y,
B, B, B, B, B, B, B, B,
B, B, Y, B, Y, B, B, B
]

sun_i2 = [
B, B, Y, B, Y, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, Y, Y, B, B, Y,
Y, B, Y, Y, Y, Y, B, B,
B, B, Y, Y, Y, Y, B, Y,
Y, B, B, Y, Y, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, Y, B, Y, B, B
]

while True:
    sense.set_pixels(sun)
    time.sleep(1)
    sense.set_pixels(sun_i1)
    time.sleep(1)
    sense.set_pixels(sun_i2)
    time.sleep(1)
'''