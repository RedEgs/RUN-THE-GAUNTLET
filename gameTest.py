from textual import on
from rich.console import Console
from rich.segment import Segment
from textual import events
from textual.events import Key, DescendantFocus, DescendantBlur, Focus, Blur, Hide, Show
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.screen import Screen
from textual.widget import Widget
from textual.containers import Horizontal, Vertical, Grid, VerticalScroll, Container
from textual.widgets import (
    Static,
    Button,
    Input,
    Label,
    ListView,
    ListItem,
    Markdown,
    Header,
    Placeholder,
    Tabs,
    TabPane,
    TabbedContent,
    Tab,
    ProgressBar,
    Rule,
    Footer,
    ContentSwitcher
)
from textual.keys import Keys
from textual import _easing

from rich.text import Text
from rich_pixels import Pixels
from rich.console import Console

from Libraries.redegsTextual import *
from Libraries.redegsGameSystems import *

import Libraries.PlayerSystem as playerSystem
import Libraries.ItemSystem as ItemSystem


AudioEngine = Audio()
AudioEngine.load()


class App(App[None]):  # Main game class containing and handling the game
    CSS_PATH = "stylesheet.tcss"  # The path of the stylesheet

    player = playerSystem.InitPlayer()

    currentInventoryList = None

    gSwitched = False

    # SECTION - Compose Result
    # * Posts widgets to the final application. Basically renders them.

    def compose(self) -> ComposeResult:
        with Grid(classes="container"):
            # SECTION - Container Initialisation
            self.One = Container(id="one")
            self.One.border_title = "Status Info"

            self.Two = Container(id="two")
            self.Two.border_title = "Game Log"

            self.Three = Container(id="three")
            self.Three.border_title = "Player & Equipment Info"

            self.Four = Container(id="four")
            self.Four.border_title = "Inventory"
            #!SECTION

            # SECTION - Status Info
            with self.One:
                maxHealth = self.player.body.body["maxHealth"]
                health = self.player.body.body["health"]

                maxMana = self.player.body.body["maxMana"]
                mana = self.player.body.body["mana"]

                maxStamina = self.player.body.body["maxStamina"]
                stamina = self.player.body.body["stamina"]

                self.hpBar = ProgressBar(
                    total=maxHealth, show_percentage=False, show_eta=False, id="hp"
                )
                self.hpBar.advance(maxHealth)
                yield Label(f"Health ({health}/{self.hpBar.total}): ")
                yield self.hpBar

                self.fpBar = ProgressBar(
                    total=maxMana, show_percentage=False, show_eta=False, id="fp"
                )
                self.fpBar.advance(maxMana)
                yield Label(f"Mana ({maxMana}/{self.fpBar.total}): ")
                yield self.fpBar

                self.stamBar = ProgressBar(
                    total=maxStamina, show_percentage=False, show_eta=False, id="stam"
                )
                self.stamBar.advance(maxStamina)
                yield Label(f"Stamina ({maxStamina}/{self.stamBar.total}): ")
                yield self.stamBar
            #!SECTION

            # SECTION - Main Gamebox
            with self.Two:
                self.presentOption = Static(
                    f"Red Pill Or Blue Pill?", id="PresentOption"
                )
                self.presentOption.border_title = "Dialogue"
                yield self.presentOption

                yield ListView(
                    NewListItem("Temp Option 1", 1, classes="menuListItem"),
                    NewListItem("Temp Option 2", 1, classes="menuListItem"),
                    NewListItem("Temp Option 3", 1, classes="menuListItem"),
                    NewListItem("Temp Option 4", 1, classes="menuListItem"),
                    id="ListOptions",
                ).add_class("hiddenSelector")
            #!SECTION

            # SECTION - Player and Equipment Info
            with self.Three:
                self.equippedContainer = Container(id="equippedOptions")
                with self.equippedContainer:
                    equippedItems = (
                        self.player.getBody().getPlayerInventory().EquippedItems
                    )
                    equippedArmour = (
                        self.player.getBody().getPlayerInventory().EquippedArmour
                    )

                    itemsOptions = ListView(id="EquippedItems")
                    itemsOptions.add_class("hiddenSelector")
                    with itemsOptions:
                        for key, value in equippedItems.items():
                            yield NewListItem(
                                f"{key} : {value}", 1, classes="menuListItem"
                            )
                        for key, value in equippedArmour.items():
                            yield NewListItem(
                                f"{key} : {value}", 1, classes="menuListItem"
                            )
            #!SECTION

            # SECTION - Inventory
            with self.Four:
                inventory = self.player.getBody().getPlayerInventory()

                # Materials, Items, Consumables, Weapons, Armour
                # --->

                self.MaterialList = ListView(
                    id="MaterialList").add_class("hiddenSelector")
                self.ItemsList = ListView(
                    id="ItemsList").add_class("hiddenSelector")
                self.ConsumablesList = ListView(
                    id="ConsumablesList").add_class("hiddenSelector")
                self.WeaponsList = ListView(
                    id="WeaponsList").add_class("hiddenSelector")
                self.ArmourList = ListView(
                    id="ArmourList").add_class("hiddenSelector")
                self.InventoryList = ListView(
                    id="InventoryList").add_class("hiddenSelector")
                #######

                self.InventoryTab = ContentSwitcher(
                    initial="InventoryContainer")

                yield Static("< All >", id="inventoryType")

                self.invContainer = Vertical(id="inventoryVert")
                with self.invContainer:
                    with self.InventoryTab:
                        with Container(id="MaterialContainer"):
                            yield Static(" SLT | NAME          | CNT | WGT         ")
                            yield Rule(id="underline")

                            yield self.MaterialList
                        with Container(id="ItemsContainer"):
                            yield Static(" SLT | NAME          | CNT | WGT         ")
                            yield Rule(id="underline")

                            yield self.ItemsList
                        with Container(id="ConsumablesContainer"):
                            yield Static(" SLT | NAME          | CNT | WGT         ")
                            yield Rule(id="underline")

                            yield self.ConsumablesList
                        with Container(id="WeaponsContainer"):
                            yield Static(" SLT | NAME          | CNT | WGT         ")
                            yield Rule(id="underline")

                            yield self.WeaponsList
                        with Container(id="ArmourContainer"):
                            yield Static(" SLT | NAME          | CNT | WGT         ")
                            yield Rule(id="underline")

                            yield self.ArmourList
                        with Container(id="InventoryContainer"):
                            yield Static(" SLT | NAME          | CNT | WGT         ")
                            yield Rule(id="underline")

                            yield self.InventoryList

                self.invInfo = Container(id="invContainer")
                with self.invInfo:
                    yield Static("Item Name: None Selected", id="ItmName")
                    yield Static("Item Description: None Selected", id="ItmDesc")
                    yield Static("Item Count: None Selected ", id="ItmCount")
                    yield Static("Item Weight: None Selected ", id="ItmWeight")
                    yield Static("Gold Coins: N/A", id="GoldAmount")

                for listview in self.query("ListView"):
                    if listview.id == "ListOptions":
                        pass
                    else:
                        listview.toggle_class("hiddenSelector")
                        listview.add_class("ImprovedList")

            #!SECTION
    #!SECTION

    # SECTION - Inventory Handling
    # * Handles Textual related Inventory Stuff

    # NOTE - Equals the first default inventory that is selected

    def appendInv(self, item):
        playerInventory = self.player.getBody().getPlayerInventory()
        stored = playerInventory.storeItem(item)
        itemType = item.itemType

        # --------

        if itemType == "material":
            if stored:
                # " SLT | NAME          | CNT | WGT         "
                self.query_one("#MaterialList").append(NewListItem(
                    f"{self.fixName(str(item.slot), 3)}| {self.fixName(item.name, 14)}|  {self.fixName(str(item.itemCount), 3)}| {item.weight} ", 2, id=f"item{item.slot}", classes="invListItem"))
                self.query_one("#InventoryList").append(NewListItem(
                    f"{self.fixName(str(item.slot), 3)}| {self.fixName(item.name, 14)}|  {self.fixName(str(item.itemCount), 3)}| {item.weight} ", 2, id=f"item{item.slot}", classes="invListItem"))
            else:
                pass

        elif itemType == "item":
            if stored:

                self.query_one("#ItemsList").append(NewListItem(
                    f"{self.fixName(str(item.slot), 3)}| {self.fixName(item.name, 14)}|  {self.fixName(str(item.itemCount), 3)}| {item.weight} ", 2, id=f"item{item.slot}", classes="invListItem"))
                self.query_one("#InventoryList").append(NewListItem(
                    f"{self.fixName(str(item.slot), 3)}| {self.fixName(item.name, 14)}|  {self.fixName(str(item.itemCount), 3)}| {item.weight} ", 2, id=f"item{item.slot}", classes="invListItem"))
            else:
                pass

        elif itemType == "consumable":

            if stored:

                self.query_one("#ConsumablesList").append(NewListItem(
                    f"{self.fixName(str(item.slot), 3)}| {self.fixName(item.name, 14)}|  {self.fixName(str(item.itemCount), 3)}| {item.weight} ", 2, id=f"item{item.slot}", classes="invListItem"))
                self.query_one("#InventoryList").append(NewListItem(
                    f"{self.fixName(str(item.slot), 3)}| {self.fixName(item.name, 14)}|  {self.fixName(str(item.itemCount), 3)}| {item.weight} ", 2, id=f"item{item.slot}", classes="invListItem"))
            else:
                pass

        elif itemType == "weapon":
            if stored:

                self.query_one("#WeaponsList").append(NewListItem(
                    f"{self.fixName(str(item.slot), 3)}| {self.fixName(item.name, 14)}|  {self.fixName(str(item.itemCount), 3)}| {item.weight} ", 2, id=f"item{item.slot}", classes="invListItem"))
                self.query_one("#InventoryList").append(NewListItem(
                    f"{self.fixName(str(item.slot), 3)}| {self.fixName(item.name, 14)}|  {self.fixName(str(item.itemCount), 3)}| {item.weight} ", 2, id=f"item{item.slot}", classes="invListItem"))
            else:
                pass

        elif itemType == "armour":
            if stored:

                self.query_one("#ArmourList").append(NewListItem(
                    f"{self.fixName(str(item.slot), 3)}| {self.fixName(item.name, 14)}|  {self.fixName(str(item.itemCount), 3)}| {item.weight} ", 2, id=f"item{item.slot}", classes="invListItem"))
                self.query_one("#InventoryList").append(NewListItem(
                    f"{self.fixName(str(item.slot), 3)}| {self.fixName(item.name, 14)}|  {self.fixName(str(item.itemCount), 3)}| {item.weight} ", 2, id=f"item{item.slot}", classes="invListItem"))
            else:
                pass

    def loadMaterialList(self, index):
        if self.player.getBody().getPlayerInventory().getSlot(str(index)) is not None:
            item = self.player.getBody().getPlayerInventory().getSlot(str(index))
            print(item)
            self.query_one("#ItmName").update(f"Item Name: {item['name']}")
            self.query_one("#ItmDesc").update(
                f"Item Description: {item['itemDesc']}")
            self.query_one("#ItmCount").update(
                f"Item Count: {item['itemCount']}")
            self.query_one("#ItmWeight").update(
                f"Item Weight: {item['weight']}")
        else:
            print("Skipped Item")

    #!SECTION

    # SECTION - Generally Other Events
    # * Contains Other Events. For example blur, focus etc.

    # NOTE - For hiddenSelector Handling
    def on_descendant_blur(self, event) -> None:

        if event.widget.id is None:
            pass
        else:
            if self.gSwitched == True:
                if event.widget.id == "MaterialList":
                    self.screen.set_focus(self.query_one("#ItemsList"))
                elif event.widget.id == "ItemsList":
                    self.screen.set_focus(self.query_one("#ConsumablesList"))
                elif event.widget.id == "ConsumablesList":
                    self.screen.set_focus(self.query_one("#WeaponsList"))
                elif event.widget.id == "WeaponsList":
                    self.screen.set_focus(self.query_one("#ArmourList"))
                elif event.widget.id == "ArmourList":
                    self.screen.set_focus(self.query_one("#InventoryList"))
                elif event.widget.id == "InventoryList":
                    self.screen.set_focus(self.query_one("#MaterialList"))

                self.gSwitched = False
            else:
                pass

        self.query_one(f"#{event.widget.id}").toggle_class("hiddenSelector")

    def on_descendant_focus(self, event) -> None:
        self.query_one(f"#{event.widget.id}").toggle_class("hiddenSelector")

    #!SECTION

    # SECTION - Shortcut Events
    # * Events for handling all shortcuts.

    def key_f(self) -> None:
        ironBar = ItemSystem.Item(
            "Iron Bar", "12", "A Big Iron Bar", "material")
        ironSword = ItemSystem.Item("Iron Sword", "5", "Big sword", "weapon")
        manaPotion = ItemSystem.Item(
            "Mana Potion", "0.4", "Restores Mana", "consumable")
        ironHelmet = ItemSystem.Item(
            "Iron Helmet", "1.2", "Gives 10 Defense", "armour")
        glassBall = ItemSystem.Item(
            "Glass Ball", "0.7", "Does Glass Things", "item")

        self.appendInv(ironBar)
        self.appendInv(ironSword)
        self.appendInv(manaPotion)
        self.appendInv(ironHelmet)
        self.appendInv(glassBall)

    currentTabTracker = 6

    def key_g(self) -> None:
        self.gSwitched = True
        self.switchInvTabs()

        if self.ItemSelected == False:
            self.loadMaterialList(self.extractInt(
                str(self.currentInventoryList.highlighted_child.id)))

    keyhTracker = True

    def key_h(self) -> None:
        if self.keyhTracker == True:
            self.query_one("#invContainer").styles.visibility = "hidden"
            self.query_one(f"#inventoryVert").styles.height = "90%"
            self.keyhTracker = False

        elif self.keyhTracker == False:
            self.query_one("#invContainer").styles.visibility = "visible"
            self.query_one(f"#inventoryVert").styles.height = "45%"
            self.keyhTracker = True

    def key_tab(self) -> None:
        self.screen.focus_next("ListView")

    #!SECTION

    # SECTION - Highlighting and Selection Handling
    # * Events for Handling List Views, Buttons etc.

    @on(ListView.Highlighted)  # Updates Any of the list views on highlight
    def HighlightUpdate(self, event: ListView.Highlighted) -> None:
        if event is None or event.list_view.index is None:
            pass
        else:
            index = self.extractInt(str(event.list_view.highlighted_child.id))

            if self.ItemSelected == False:
                self.loadMaterialList(self.extractInt(
                    str(event.list_view.highlighted_child.id)))
            else:
                pass

            print(f"current ListView = {event.list_view}")
            print(f"current Item Number = {index}")
            print(f"item selected = {index}")

    @on(ListView.Highlighted)  # Handles audio to do with list views
    def HighlightAudio(self, event: ListView.Highlighted) -> None:
        AudioEngine.playSound("click1")

    ItemSelected = False
    selectedItem = None

    # Handles ListItem Selection for the inventory + Audio Selection
    @on(ListView.Selected)
    def selectHandler(self, event: ListView.Selected) -> None:
        AudioEngine.playSound("click6")

        # Prints the parent of the container
        print(f"parent = {event.item.parent.parent}")
        if event.item.parent.parent.id is not "InventoryContainer":
            pass  # Passes if its not an inventory container.
        else:
            if self.ItemSelected == True and self.selectedItem.id == event.item.id:
                self.query(f"#{self.selectedItem.id}").toggle_class(
                    "--selected")
                self.ItemSelected = False
                self.selectedItem = None

            elif self.ItemSelected == False or self.selectedItem is None:
                print(event.item.id)
                self.query(f"#{event.item.id}").toggle_class("--selected")
                self.ItemSelected = True
                self.selectedItem = event.item

                self.loadMaterialList(event.list_view.index + 1)

            elif self.selectedItem.id != event.item.id:
                print(event.item.id)
                self.query(f"#{self.selectedItem.id}").toggle_class(
                    "--selected")
                self.query(f"#{event.item.id}").toggle_class("--selected")
                self.ItemSelected = True
                self.selectedItem = event.item

                self.loadMaterialList(event.list_view.index + 1)

    #!SECTION

    # SECTION - Random Functions

    def switchInvTabs(self):
        AudioEngine.playSound("switch35")

        if self.currentTabTracker == 1:
            self.query_one("#inventoryType").update("< Materials >")
            self.currentTabTracker = 2

            self.query_one(ContentSwitcher).current = "MaterialContainer"
            self.currentInventoryList = self.query_one("#MaterialList")
            self.loadMaterialList(self.currentInventoryList.index)

        elif self.currentTabTracker == 2:
            self.query_one("#inventoryType").update("< Items >")
            self.currentTabTracker = 3

            self.query_one(ContentSwitcher).current = "ItemsContainer"
            self.currentInventoryList = self.query_one("#ItemsList")
            self.loadMaterialList(self.currentInventoryList.index)

        elif self.currentTabTracker == 3:
            self.query_one("#inventoryType").update("< Consumables >")
            self.currentTabTracker = 4

            self.query_one(ContentSwitcher).current = "ConsumablesContainer"
            self.currentInventoryList = self.query_one("#ConsumablesList")
            self.loadMaterialList(self.currentInventoryList.index)

        elif self.currentTabTracker == 4:
            self.query_one("#inventoryType").update("< Weapons >")
            self.currentTabTracker = 5

            self.query_one(ContentSwitcher).current = "WeaponsContainer"
            self.currentInventoryList = self.query_one("#WeaponsList")
            self.loadMaterialList(self.currentInventoryList.index)

        elif self.currentTabTracker == 5:
            self.query_one("#inventoryType").update("< Armour >")
            self.currentTabTracker = 6

            self.query_one(ContentSwitcher).current = "ArmourContainer"
            self.currentInventoryList = self.query_one("#ArmourList")
            self.loadMaterialList(self.currentInventoryList.index)

        elif self.currentTabTracker == 6:
            self.query_one("#inventoryType").update("< All >")
            self.currentTabTracker = 1

            self.query_one(ContentSwitcher).current = "InventoryContainer"
            self.currentInventoryList = self.query_one("#InventoryList")
            self.loadMaterialList(self.currentInventoryList.index)

    #!SECTION

    # ANCHOR - on_mount()
    # * First thing ran on startup
    def on_mount(self) -> None:
        FullscreenApplication()


if __name__ == "__main__":  # Runs the game on script start up
    program = App()
    program.run()
