from rich.console import Console
from rich.segment import Segment
from textual import events
from textual.events import Key
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Static, Button, Input, Label, ListView, ListItem
from textual.keys import Keys
from textual import _easing
from rich.text import Text
import climage, random

import os, sys, time, asyncio

class Cutscene2(Screen):
    def compose(self):
        self.title = Static("WHAT IS YOUR NAME?", id="title2")
        yield self.title

        self.title2 = Static("MY NAME IS : PLACEHOLDER", id="middleText")
        yield self.title2
        

    def on_mount(self):
        self.title.styles.opacity = 0.0
        self.title2.styles.opacity = 0.0

        self.title.styles.animate("opacity", value=1.0, duration=1.0)
        self.title2.styles.animate("opacity", value=1.0, duration=1.0, delay=1)

class Cutscene1(Screen):
    animation_completed = False  # Flag to track animation completion
    
    def compose(self):
        self.title = Static("ARE YOU READY TO RUN THE GAUNTLET", id="title")
        self.subtitle = Static("PRESS ANY [green][KEY][white] TO CONTINUE", id="any-key")
        yield self.title
        yield self.subtitle

    def on_mount(self):
        self.title.styles.opacity = 0.0
        self.subtitle.styles.opacity = 0.0
        self.title.styles.animate("opacity", value=1.0, duration=1.0)
        self.subtitle.styles.animate("opacity", value=1.0, duration=1.0, delay=1, on_complete=lambda: self.set_animation_completed())

    def set_animation_completed(self):
        self.animation_completed = True  

    def _on_key(self, event: Key) -> None:
        if self.animation_completed:    
            self.title.styles.animate("opacity", value=0.0, duration=1.0)
            self.subtitle.styles.animate("opacity", value=0.0, duration=1.0, delay=1, on_complete=lambda: app.switch_screen(screen="cut2"))

class App(App): # Main game class containing and handling the game

    CSS_PATH = "stylesheet.tcss" # The path of the stylesheet
    SCREENS = {"cut1": Cutscene1(), "cut2" : Cutscene2()} # Initialises and organises the screen stack
    # Screen stack started left to right in sequence
    
    def on_mount(self) -> ComposeResult: # When the program is first launched >>
        self.push_screen(screen="cut1") # Start the first cutscene (Contained as a screen)

        

    

if __name__ == "__main__": # Runs the game on script start up
    app = App() # Starts the game class
    app.run() # Runs the initialised class