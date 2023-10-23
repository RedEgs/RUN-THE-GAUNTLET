from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import ListView, ListItem, Label, ContentSwitcher, Rule
from textual.events import Focus, Click, DescendantFocus
from redegsTextual import *

class app(App[None]):
    def compose(self) -> ComposeResult:


        self.InventoryTab = ContentSwitcher(initial="MaterialContainer")
        yield Static("< Materials >", id="inventoryType")

        self.invContainer = Vertical(id="inventoryVert")
        with self.invContainer:
            with self.InventoryTab:
                with Container(id="MaterialContainer"):
                    yield Static(" Materials")
                    yield Rule(id="underline")

                    yield ListView(
                        ListItem(Label("Material 1")),
                        ListItem(Label("Material 2")),
                        ListItem(Label("Material 3"))
                    )

                with Container(id="ItemsContainer"):
                    yield Static(" Items ")
                    yield Rule(id="underline")

                    yield ListView(
                        ListItem(Label("Items 1")),
                        ListItem(Label("Items 2")),
                        ListItem(Label("Items 3"))
                    )

                with Container(id="ConsumablesContainer"):
                    yield Static(" Consumables ")
                    yield Rule(id="underline")

                    yield ListView(
                        ListItem(Label("Consumables 1")),
                        ListItem(Label("Consumables 2")),
                        ListItem(Label("Consumables 3"))
                    )          


    def key_g(self) -> None:
        self.query_one(ContentSwitcher).current = "ItemsContainer"


if __name__ == "__main__":
    app().run()