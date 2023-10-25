from textual import on
from typing import Any, Coroutine
from rich.console import Console, RenderableType
from rich.segment import Segment
from textual import events
from textual.events import Key, DescendantFocus, DescendantBlur, Focus, Blur
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Static, Button, Input, Label, ListView, ListItem, Markdown, Header
from textual.keys import Keys
from textual import _easing
from rich.text import Text
import os


class NewListItem(ListItem):

    lastPressed = str
    DEFAULT_CSS = """

    NewListItem {
        layout: horizontal;
    }
    NewListItem .selector {
        visibility: hidden;
        color: gray;
    }
    NewListItem.--highlight .selector   {
        visibility: visible;
        color: white;
    }

    .disabledItem {
    
        color: gray;
    
    }

    .disabledItem.--highlight {
    
        color: gray;
    
    }
    """

    def __init__(self, text, selector=None, id=None, classes=None) -> None:
        super().__init__(id=id, classes=classes)
        self._text = text
        self.selector = selector
        self.selectors = [
            "",
            "><",
            "[]",
            "{}",
            "()",
            "**",
            "^^",
            "||",
            "\/",
            "--",
        ]

    def compose(self) -> ComposeResult:
        if self.selector == None:
            yield Label(f"  {self._text}  ")
        else:
            yield Label(f"{self.selectors[int(self.selector)][0]} ", classes="selector")
            yield Label(self._text)
            yield Label(f" {self.selectors[int(self.selector)][1]}", classes="selector")


def FullscreenApplication():
    import win32gui
    import win32con

    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
