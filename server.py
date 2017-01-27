from flask import Flask, request
import models
import displaySwitch

app = Flask(__name__)

@app.route("/switch-app", methods=['GET', 'POST'])
def switch():
    mode = request.form['mode']
    panel_state.set_mode(mode)
    displaySwitch.draw(panel_state)
    return "Current mode: " + panel_state.mode

@app.route("/baseball", methods=['POST'])
def baseball_state():
    return "Set baseball"

@app.route("/mbta", methods=['POST'])
def mbta_state():
    return "Set mbta"

@app.route("/weather", methods=['POST'])
def weather_state():
    return "Set weather"

def main():
    global panel_state
    panel_state = models.PanelState()
    app.run(host='0.0.0.0', port=6001)

main()
