
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Label
from textual.events import Focus, Click, DescendantFocus
from redegsTextual import *

class ListViewMessageExampleApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label("Chosen item will appear here", id="chosen")

        yield ListView(
            NewListItem("Mal", 1),
            NewListItem("Zoe", 2),
            NewListItem("Wash", ),
            NewListItem("Jayne", 1),
            NewListItem("Book",),
            #NewListItem("Simon", id="simon"),
           # NewListItem("River", id="river"),
        )

        yield NewListView(
            NewListItem("Mal", 1, id="mal"),
            NewListItem("Zoe", 2, id="zoe"),
            NewListItem("Wash", id="wash"),
            NewListItem("Jayne", 1, id="jayne"),
            NewListItem("Book", id="book"),
            NewListItem("Simon", id="simon"),
            NewListItem("River", id="river"),
        )
    def on_mount(self) -> None:
        self.query_one("#jayne", NewListItem).add_class("disabledItem")

    @on(ListView.Selected)
    def show_chosen(self, event: ListView.Selected) -> None:
        self.query_one("#chosen", Label).update(f"{event.item}")

if __name__ == "__main__":
    ListViewMessageExampleApp().run()