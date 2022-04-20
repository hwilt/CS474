import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class HomeScreen(GridLayout):

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="map"))
        self.add_widget(Label(text="home bar"))


class MyApp(App):
    
    def build(self):
        return HomeScreen()
if __name__ == '__main__':
    MyApp().run()