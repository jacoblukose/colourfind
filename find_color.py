import webcolors
from PIL import Image
import math
import os

os.system("ls *.jpg *.png")

image_name=raw_input()
obj=Image.open(image_name)
obj=obj.convert('RGB')


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

actual_name, closest_name = get_colour_name(max(obj.getcolors(obj.size[0]*obj.size[1]))[1])

print "Dominant color is "+ closest_name


