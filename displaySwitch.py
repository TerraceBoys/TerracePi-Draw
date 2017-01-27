import models
import mbtaDisplay
import baseballDisplay
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(32, 2)

def draw(panel_state):
    if panel_state.mode == "mbta":
        mbtaDisplay.main(matrix, panel_state.mbta_state, panel_state.weather_state)
    else: 
        baseballDisplay.main(matrix, panel_state.game_state)
