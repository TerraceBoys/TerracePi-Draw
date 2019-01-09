# !/usr/bin/python

import time
import traceback

import Image
import ImageDraw
import ImageFont

import models

font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf", 8)
message = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf", 22)
train = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf", 11)
weather_font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf", 10)

def main(matrix, mbta_state, weather_state):
    global draw
    image = Image.new("RGB", (64, 32))
    draw = ImageDraw.Draw(image)
    setup_board()
    train_display(mbta_state)
    weather_display(weather_state)
    weather_icon = Image.open("images/" + weather_state.jpeg)
    weather_icon.load()
    matrix.Clear()
    matrix.SetImage(image.im.id, 0, 0)
    matrix.SetImage(weather_icon.im.id, 44, 13)
            
def setup_board():
    global draw
    draw.text((2, 1), "l TERRACE", font=font, fill="white")
    draw.line((0, 0, 63, 0), fill="#400080")
    draw.line((0, 31, 63, 31), fill="#400080")
    draw.line((63, 1, 63, 30), fill="#400080")
    draw.line((40, 1, 40, 30), fill="#400080")
    draw.line((0, 1, 0, 30), fill="#400080")
    draw.line((1, 9, 39, 9), fill="#400080")

def set_weather(temp, temp_color):
    global panel_state
    panel_state['weather'] = {'temp':str(temp), 'temp_color':temp_color}

def set_mbta(schedule):
    global panel_state
    panel_state['schedule'] = schedule

def train_display(mbta_state):
    global draw
    if mbta_state.time_1:
        draw.text((4, 10), mbta_state.time_1, font=train, fill=mbta_state.color_1)
        if mbta_state.time_2:
            draw.text((4, 19), mbta_state.time_2, font=train, fill=mbta_state.color_2)
    else:
        draw.text((4, 10), "No", font=train, fill="red")
        draw.text((4, 19), "Trains", font=train, fill="red")

def weather_display(weather_state):
    global draw
    if weather_state.temp:
        print weather_state.color
        draw.text((46, 3), weather_state.temp + u"\u00b0", font=weather_font, fill=weather_state.color)
    else:
        draw.text((44, 3), "N\A", font=weather_font, fill="red")

if __name__ == "__main__":
    main()
