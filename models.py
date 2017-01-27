class PanelState:
    def __init__(self, mode="mbta"):
        self.mbta_state = MbtaState()
        self.weather_state = WeatherState()
        self.game_state = GameState()
        self.mode = mode

    def set_mode(self, mode):
        self.mode = mode

    def set_mbta_state(self, mbta_state):
        self.mbta_state = mbta_state

    def set_weather_state(self, weather_state):
        self.weather_state = weather_state

    def set_game_state(self, game_state):
        self.game_state = game_state

class MbtaState:
    def __init__(self, time_1=None, time_2=None, color_1=None, color_2=None):
        self.time_1 = time_1
        self.time_2 = time_2
        self.color_1 = color_1
        self.color_2 = color_2

class WeatherState:
    def __init__(self, temp=None, color=None, jpeg="sun2"):
        self.temp = temp
        self.color = color
        self.jpeg = jpeg

class GameState:
    def __init__(self, score1=0, score2=0, batting=0, base1=0, base2=0, base3=0, inning=1, strikes=0, outs=0):
        self.score1 = score1
        self.score2 = score2
        self.batting = batting
        self.base1 = base1
        self.base2 = base2
        self.base3 = base3
        self.inning = inning
        self.strikes = strikes
        self.outs = outs
