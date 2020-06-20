# Main code for Pomo. Joins the kivy GUI with the core functions.

from PomoFoobars import sample_func

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class PoMoApp(App): # <- Main Class
    pass

if __name__ == "__main__":
    pomo = PomoApp()
    pomo.run()
