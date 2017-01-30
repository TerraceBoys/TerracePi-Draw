import models
import mbtaDisplay
import baseballDisplay
import personPickerDisplay
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(32, 2)

def draw(panel_state, switch=False):
    if panel_state.mode == "mbta":
        mbtaDisplay.main(matrix, panel_state.mbta_state, panel_state.weather_state)
    elif panel_state.mode == "baseball":
        if switch:
            baseballDisplay.drawIntro(matrix) 
        baseballDisplay.main(matrix, panel_state.game_state)
    elif panel_state.mode == "person_picker":
        if switch:
            personPickerDisplay.drawIntro(matrix)
        else:
            personPickerDisplay.main(matrix, panel_state.person_picker_state)
    else:
        print "Invalid mode"
