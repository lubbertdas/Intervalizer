import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.recyclegridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from IntervalsRandomizer import Randomizer
     
class MyGrid(Widget):
    planet_distance = ObjectProperty(None)
    planet_diameter = ObjectProperty(None)
    planet_name = ObjectProperty(None)
    output = ObjectProperty(None)
            
    def btn(self):
        self.output.text = Randomizer()
    
class Intervaler(App):
    def build(self):
        return MyGrid()
    pass
    
if __name__ == "__main__":
    Intervaler().run()
