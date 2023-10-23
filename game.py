from textual import on
from typing import Any, Coroutine
from rich.console import Console
from rich.segment import Segment
from textual import events
from textual.events import Key
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Static, Button, Input, Label, ListView, ListItem, Markdown, Header
from textual.keys import Keys
from textual.containers import Container
from textual import _easing
from rich.text import Text
from rich_pixels import Pixels
from rich.console import Console
from redegsTextual import *
from redegsGameSystems import *
import climage, random, pyfiglet, os


class DifficultyScreen(Screen):

        
    def compose(self) -> ComposeResult:
        
        with Container():
            self.difficutlyMenu = ListView(
                NewListItem("Easy", 1,id="easyBtn"),
                NewListItem("Normal", 1, id="normalBtn"),
                NewListItem("Difficult", 1, id="difficultBtn"),
                NewListItem("Impossible", 1, id="impossibleBtn"),
                classes="mainMenuOptions"
            )   
            yield self.difficutlyMenu

        
    

class OptionScreen(Screen):
    audio = Audio()
    audio.load_sound_effects()
    
    def compose(self) -> ComposeResult:
        yield Header()
    
    def on_key(self, event: events.Key) -> None:
        if event.key == "backspace" or "esc":
            self.app.pop_screen()
            self.audio.playSound("Denied")

class IntroScreen(Screen):
    audio = Audio()
    audio.load_sound_effects()

    animFinished = False

    def compose(self) -> ComposeResult:
        self.introLabel = Static("RUN THE GAUNTLET", id="mainTitle")
        self.introLabel.styles.opacity = 0.0
        yield self.introLabel

    def onAnimFinish(self):
        self.animFinished = True

    def on_mount(self) -> None:
        self.introLabel.styles.animate("opacity", value=1.0, duration=0.5,on_complete= lambda: self.onAnimFinish())
        
    def on_key(self, event: events.Key) -> None:
        if self.animFinished:
            self.audio.playSound("Intro")
            self.introLabel.styles.animate("opacity", value=0.0, duration=1.8, on_complete=lambda: self.app.pop_screen())

class App(App[None]): # Main game class containing and handling the game
    CSS_PATH = "stylesheet.tcss" # The path of the stylesheet
    #SCREENS = {"optionScreen": OptionScreen()}

    audio = Audio()
    audio.load_sound_effects()

    lastPressed = str

    def compose(self) -> ComposeResult:
        self.listMenu = ListView(
            NewListItem("Start New Game", 1,id="startBtn"),
            NewListItem("Load Game", 1, id="loadBtn"),
            NewListItem("Options", 1, id="optionBtn"),
            NewListItem("Quit Game", 1, id="quitBtn"),
            classes="mainMenuOptions"
        )   
        yield self.listMenu

    def on_mount(self) -> None:
        self.app.install_screen(DifficultyScreen(), name="difficultyScreen")
        self.app.install_screen(OptionScreen(), name="optionScreen")
        self.app.install_screen(IntroScreen(), name="introScreen")

        savedStatus = findSave("hi.txt", f"{os.getcwd()}/saved")
        if savedStatus:
            pass
        else:
            self.query_one("#loadBtn", NewListItem).add_class("disabledList")

        self.app.push_screen("introScreen")

    @on(ListView.Selected)
    def selectHandler(self, event: ListView.Selected) -> None:
        self.audio.playSound("Confirm")

        if event.item.id == "startBtn":
            self.app.push_screen("difficultyScreen")
        elif event.item.id == "loadBtn":
            pass
        elif event.item.id == "optionBtn":
            self.app.push_screen("optionScreen")


        elif event.item.id == "quitBtn":
            self.app.exit()

    @on(ListView.Highlighted)
    def HighlightHandler(self, event: ListView.Highlighted) -> None:
        if "disabledList" in event.item.classes:
            if self.lastPressed == "down":
                event.list_view.action_cursor_down()
            elif self.lastPressed == "up":
                event.list_view.action_cursor_up()
        else:
            self.audio.playSound("Hover")
    
    def on_key(self, event: events.Key) -> None:
        self.lastPressed = event.key

if __name__ == "__main__": # Runs the game on script start up
    app = App() # Starts the game class
    app.run() # Runs the initialised class