from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data ."""
        names = ['apple', 'banana', 'cherry']
        for name in names:
            temp_label = Label(text=name, font_size=20)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
