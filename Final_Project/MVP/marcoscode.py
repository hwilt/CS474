import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy_garden.mapview import MapView
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.button import Button

Window.size = 320, 600
Builder.load_file('design.kv')

class BottomRectangle(Widget):
    pass
class Btns(FloatLayout):
    pass
class CustomLayout(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        self.icon = 'uc-logo.png'
        self.title = "Scavenger Hunt"
        main_layout = BoxLayout(orientation="vertical")
        self.map = MapView(zoom=100, lat=40.19305534071627, lon=-75.45637860497125)
        main_layout.add_widget(self.map)
        main_layout.add_widget(BottomRectangle())
        
        return main_layout
    
if __name__ == '__main__':
    MyApp().run()