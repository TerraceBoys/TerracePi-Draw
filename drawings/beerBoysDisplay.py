#!.env/bin/python

import time
import traceback

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import models

text_font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf", 9)

def main(matrix, beer_boys_state):
    image = Image.new("RGB", (64, 32))
    draw = ImageDraw.Draw(image)
    boys = beer_boys_state.people
    print boys
    print boys[1]['beers']
    if len(boys) > 0:
        draw.text([1, 8], boys[0]['name'], font=text_font, fill='orange')
        draw.text([45, 8], str(boys[0]['beers']), font=text_font, fill='orange')
    if len(boys) > 1:
        draw.text([1, 16], boys[1]['name'], font=text_font, fill='white')
        draw.text([45, 16], str(boys[1]['beers']), font=text_font, fill='white')
    if len(boys) > 2:
        draw.text([1, 0], boys[2]['name'], font=text_font, fill='purple')
        draw.text([45, 0], str(boys[2]['beers']), font=text_font, fill='purple')
    if len(boys) > 3:
        draw.text([1, 24], boys[3]['name'], font=text_font, fill='green')
        draw.text([45, 24], str(boys[3]['beers']),  font=text_font, fill='green')
    matrix.Clear()
    matrix.SetImage(image.im.id, 0, 0)

if __name__ == "__main__":
    main(None)
