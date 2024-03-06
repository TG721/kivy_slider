from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('design.kv')
class MyLayout(Widget):
    def on_slide(self, *args):
     self.ids.async_image.size_hint_x = float(args[1]/100)

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()