import models
import mbtaDisplay
import baseballDisplay
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(32, 2)

def draw(panel_state, switch=False):
    if panel_state.mode == "mbta":
        mbtaDisplay.main(matrix, panel_state.mbta_state, panel_state.weather_state)
    elif panel_state.mode == "baseball":
        if switch:
            baseballDisplay.drawIntro(matrix) 
        baseballDisplay.main(matrix, panel_state.game_state)
    else:
        print "Invalid mode"
