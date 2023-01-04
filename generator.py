from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt
from PIL import Image 

"""
?Params structure:
- params is a list which contains all the data that we need to generate our map
- 0 -> the width of the map
- 1 -> the height of the map
"""

def GenerateMap(params):
    width = int(params[0])
    height = int(params[1])

    map, minmax = FillWithPixels(width,height)
    img = Image.new("RGB",(width,height), color="white")

    pixels = img.load()

    for y in range(0,height):
        for x in range(0,width):
            if map[y][x] > minmax[0]+0.4:
                img.putpixel((y,x),(0,0,255))
            elif(abs(map[y][x] - (minmax[0]+0.4)) < 0.05):
                img.putpixel((y,x),(255,255,51))
            elif(abs(map[y][x] - (minmax[1]-0.1) > 0.1)):
                img.putpixel((y,x),(51,51,51))
            else:
                img.putpixel((y,x),(0,255,0))

    img.save("teszt.png")
    img.show()
#___________________________________________________________________________________________________#

def FillWithPixels(width,height):
    noise1 = PerlinNoise(octaves=3)
    noise2 = PerlinNoise(octaves=6)
    noise3 = PerlinNoise(octaves=12)
    noise4 = PerlinNoise(octaves=24)

    xpix, ypix = width,height
    pic = []
    for i in range(xpix):
        row = []
        for j in range(ypix):
            noise_val = noise1([i/xpix, j/ypix])
            noise_val += 0.5 * noise2([i/xpix, j/ypix])
            noise_val += 0.25 * noise3([i/xpix, j/ypix])
            noise_val += 0.125 * noise4([i/xpix, j/ypix])

            row.append(noise_val)
        pic.append(row)

    min_y = 10
    max_y = -10
    for row in pic:
        for v in row:
            if v > max_y:
                max_y = v
            if v < min_y:
                min_y = v

    print(f"min: {min_y} max: {max_y}")

    return pic, (min_y,max_y)