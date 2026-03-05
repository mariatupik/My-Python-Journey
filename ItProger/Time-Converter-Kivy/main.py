from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (360, 640)

class Container(GridLayout):
    def convert(self):
        try:
            number = int(self.text_input.text)
        except Exception:
            number = 0
        self.label_hours.text = str(number*24)
        self.label_minutes.text = str(number*24*60)
        self.label_seconds.text = str(number*24*60*60)
        self.label_milliseconds.text = str(number*24*60*60*1000)
        self.label_weeks.text = "{:.2f}".format(number / 7)


class Duckyapp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    Duckyapp().run()