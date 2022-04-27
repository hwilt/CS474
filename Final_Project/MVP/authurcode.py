import kivy
kivy.require('2.1.0') # replace with your current kivy version !
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
from kivy.graphics.texture import Texture
import geocoder
import os

Window.size = 320, 600
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

screen_helper = """

ScreenManager:
    MapScreen:
    AchievementScreen:
    HelpScreen:
    CameraScreen:
    
<AchievementScreen>:
    name: 'ach'
    canvas.before:
        Color:
            rgba:  252/255.0, 176/255.0, 52/255.0, 1
        Rectangle:
            size: self.size
            pos: self.pos

    MDLabel:
        text: 'Achievements'
        halign: 'center'
    RelativeLayout:
        size_hint_y: None
        height: dp(50)
        canvas:
            Color:
                rgba: 252/255.0, 176/255.0, 52/255.0, 1
            Rectangle:
                size: self.size
        AwardButton:
            source: 'arrow.png'
            keep_ratio: False
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: None, None # if you are setting the size, the hint must be set to None
            size: 40, 40
            on_release: root.manager.current = 'map'
    GridLayout:
        cols:3
        size: root.width,root.height
        Label:
            text:"image"
        Label:
            text:"image"
        Label:
            text:"image"
        Label:
            text:"image"
        Label:
            text:"image"

        
<HelpScreen>:
    name: 'help'
    canvas.before:
        Color:
            rgba: 88/255.0, 0/255.0, 0/255.0, 1
        Rectangle:
            size: self.size
            pos: self.pos

    MDLabel:
        text: 'Help'
        halign: 'center'
    RelativeLayout:
        size_hint_y: None
        height: dp(50)
        canvas:
            Color:
                rgba: 252/255.0, 176/255.0, 52/255.0, 1
            Rectangle:
                size: self.size
        AwardButton:
            source: 'arrow.png'
            keep_ratio: False
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: None, None # if you are setting the size, the hint must be set to None
            size: 40, 40
            on_release: root.manager.current = 'map'

<MapScreen>:
    name: 'map'
    MapView:
        zoom: 100
        lat: 40.19305534071627
        lon: -75.45637860497125
        double_tap_zoom: True
        size: self.size
        MapMarkerPopup:
            source: 'marker.png'
            
            size: 30, 30
            MDLabel:
                id: 'FLB'
                text: "FLB"
        
        MapMarkerPopup:
            source: 'marker.png'
            lat: 40.19442397231081
            lon: -75.45833125312626
            size: 30, 30
            Label:
                id: 'Kaleidoscope Performing Arts Center'
                text: 'Kaleidoscope Performing Arts Center'
                color: (0, 0, 0, 1)

        MapMarkerPopup:
            source: 'marker.png'
            lat: 40.19305534071627
            lon: -75.45637860497125
            size: 30, 30
            Label:
                id: 'Wismer Center Dining Hall'
                text: 'Wismer Center Dining Hall'
                color: (0, 0, 0, 1)

        MapMarkerPopup:
            source: 'marker.png'
            lat: 40.19206368018941
            lon: -75.45708134372097
            size: 30, 30
            Label:
                id: 'Bomberger Hall'
                text: 'Bomberger Hall'
                color: (0, 0, 0, 1)
        MapMarkerPopup:
            source: 'marker.png'
            lat: 40.19245706791343
            lon: -75.45670047004295
            size: 30, 30
            Label:
                id: 'Olin Hall'
                text: 'Olin Hall'
                color: (0, 0, 0, 1)

        MapMarkerPopup:
            source: 'marker.png'
            lat: 40.19464114783587
            lon: -75.45574560363646
            size: 30, 30
            Label:
                id: 'Ritter Hall'
                text: 'Ritter Hall'
                color: (0, 0, 0, 1)

        MapMarkerPopup:
            source: 'marker.png'
            lat: 40.192473459026864
            lon: -75.4572851916091
            size: 30, 30
            Label:
                id: 'Myrin Library'
                text: 'Myrin Library'
                color: (0, 0, 0, 1)

        MapMarkerPopup:
            source: 'marker.png'
            lat: 40.1911375708896
            lon: -75.45615866382441
            size: 30, 30
            Label:
                id: 'Schellhase Commons'
                text: 'Schellhase Commons'
                color: (0, 0, 0, 1)

        MapMarkerPopup:
            source: 'marker.png'
            lat: 40.191985821902584
            lon: -75.45630886752811
            size: 30, 30
            Label:
                id: 'Berman Museum'
                text: 'Berman Museum'
                color: (0, 0, 0, 1)
            

    RelativeLayout:
        size_hint_y: None
        height: dp(50)
        canvas:
            Color:
                rgba: 252/255.0, 176/255.0, 52/255.0, 1
            Rectangle:
                size: self.size
        AwardButton:
            source: 'award.png'
            keep_ratio: False
            pos_hint: {'right': 1, 'center_y': .5}
            size_hint: None, None # if you are setting the size, the hint must be set to None
            size: 40, 40
            on_release: root.manager.current = 'ach'
        AwardButton:
            source: 'question.png'
            keep_ratio: False
            pos_hint: {'left': 1, 'center_y': .5}
            size_hint: None, None # if you are setting the size, the hint must be set to None
            size: 40, 40
            on_release: root.manager.current = 'help'
        AwardButton:
            source: 'camera.png'
            keep_ratio: False
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: None, None # if you are setting the size, the hint must be set to None
            size: 40, 40
            on_release: root.manager.current = 'cam'

<CameraScreen>:
    name: 'cam'
    Camera:
        id: camera
        index: 0
        resolution: (-1, -1)
        play: True
    RelativeLayout:
        size_hint_y: None
        height: dp(50)
        canvas:
            Color:
                rgba: 252/255.0, 176/255.0, 52/255.0, 1
            Rectangle:
                size: self.size
        AwardButton:
            source: 'arrow.png'
            keep_ratio: False
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: None, None # if you are setting the size, the hint must be set to None
            size: 40, 40
            on_release: root.manager.current = 'map'
"""



class AchievementScreen(Screen):
    pass

class Achievements(GridLayout):
    pass
class HelpScreen(Screen):
    pass

class MapScreen(Screen):
    pass
class CameraScreen(Screen):
    pass

class Blank(Image):
    pass

class AwardButton(ButtonBehavior, Image):  # the Award button is an image, added button behavior
    pass

sm = ScreenManager()
sm.add_widget(MapScreen(name='map'))
sm.add_widget(AchievementScreen(name='ach'))
sm.add_widget(HelpScreen(name='help'))
sm.add_widget(CameraScreen(name='cam'))



class MyApp(MDApp):
    def build(self):
        
        screen = Builder.load_string(screen_helper)
        self.icon = 'uc-logo.png'
        self.title = "Scavenger Hunt"
        
        return screen

MyApp().run()