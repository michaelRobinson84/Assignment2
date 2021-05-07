from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertMilesKm(App):

    def build(self):

        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, upDownAmount):

        value_to_convert = self.get_valid_miles()
        value_to_convert = value_to_convert + upDownAmount


        self.root.ids.input_in_miles.text = str(value_to_convert)

    def handle_text_change(self):

        value_to_convert = self.get_valid_miles()

        self.root.ids.input_in_miles.text = str(value_to_convert)

        self.root.ids.output_label.text = str(value_to_convert * MILES_TO_KM)


    def get_valid_miles(self):

        try:
            value = int(self.root.ids.input_in_miles.text)
            return value
        except ValueError:
            return 0

    def convert_miles_to_kilometres(self):

        value_to_display = float(self.root.ids.input_in_miles.text) * MILES_TO_KM
        self.root.ids.output_label.text = str(value_to_display)

ConvertMilesKm().run()