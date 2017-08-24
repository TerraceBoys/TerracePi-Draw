from flask import Flask, request
import models
import displaySwitch
import time

app = Flask(__name__)

@app.route("/switch-app", methods=['GET', 'POST'])
def switch():
    mode = request.form['mode']
    if mode == "mbta":
        panel_state.set_mode(mode)
    elif mode == "baseball":
        panel_state.set_mode(mode)
        update_game_state(request)
    elif mode == "person_picker":
        panel_state.set_mode(mode)
    else:
        return "Invalid mode"
    
    displaySwitch.draw(panel_state, True)
    return "Current mode: " + panel_state.mode

@app.route("/baseball", methods=['POST'])
def baseball_state():
    update_game_state(request)
    if panel_state.mode == "baseball":
        displaySwitch.draw(panel_state)

    return "Set baseball"

def update_game_state(request):
    game_state = models.GameState(
    request.form['score1'],
    request.form['score2'],
    request.form['batting'],
    request.form['base1'],
    request.form['base2'],
    request.form['base3'],
    request.form['inning'],
    request.form['strikes'],
    request.form['outs'])

    panel_state.set_game_state(game_state)

@app.route("/mbta", methods=['POST'])
def mbta_state():
    print request.form

    mbta_state = models.MbtaState(
    request.form['time_1'],
    request.form['time_2'],
    request.form['color_1'],
    request.form['color_2'])

    print "Made mbtaState"
    panel_state.set_mbta_state(mbta_state)
    if panel_state.mode == "mbta":
        displaySwitch.draw(panel_state)

    return "Set mbta"

@app.route("/weather", methods=['POST'])
def weather_state():
    color = (int(request.form['r']), int(request.form['g']), int(request.form['b']))
    weather_state = models.WeatherState(
    request.form['temp'],
    color,
    request.form['jpeg'])

    panel_state.set_weather_state(weather_state)
    if panel_state.mode == "mbta":
        displaySwitch.draw(panel_state)
    return "Set weather"

@app.route("/person-picker", methods=['POST'])
def person_picker_state():
    people = request.form.getlist('people')
    print people
    person_picker_state = models.PersonPickerState(people, request.form['chosen_index'])
    panel_state.set_person_picker_state(person_picker_state)
    displaySwitch.draw(panel_state)    
    return 'Set Person Picker'

def main():
    global panel_state
    panel_state = models.PanelState()
    displaySwitch.draw(panel_state)
    time.sleep(10)
    app.run(host='0.0.0.0', port=6001)

main()
