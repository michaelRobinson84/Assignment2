from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabels(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.names = ["Michael", "Anthony", "Robinson"]

    def build(self):

        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.display_labels()

        return self.root

    def display_labels(self):
        for name in self.names:

            temp_label = Label(text=name)

            self.root.ids.main.add_widget(temp_label)

DynamicLabels().run()