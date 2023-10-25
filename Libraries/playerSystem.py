import random
import time
import ItemSystem


def InitPlayer():
    pProp = PlayerProperties()
    pInv = PlayerInventory()
    body = Body(pProp, pInv)
    player = Player(body)

    return player


def randomName():
    file = open("nametable.txt", "r")
    name = file.readline(random.randint(1, 25))

    return name


class PlayerProperties:
    """
    Contains all properties of a player such as skills and talents.
    """

    def __init__(self):
        self.skills = {
            "manaPower": 0,
            "intelligence": 0,
            "speed": 0,
            "accuracy": 0,
            "strength": 0,
            "luck": 0,
        }

        self.talents = {
            "melee": 0,
            "aiming": 0,
            "magic": 0,
            "stealth": 0,
            "sight": 0,
            "perception": 0,
        }

    def setSkill(self, skill, value):
        if value > 20:
            self.skills = self.skills[skill] = value
        elif value < 20:
            self.skills = 20

    def setTalent(self, talent, value):
        if value > 20:
            self.talent = self.talents[talent] = value
        elif value < 20:
            self.talent = 20

    def scaleTalent(self, talent):
        """
        Returns the string version of a talent from an integer.
        """

        if int < 3:
            return "POOR"
        if int < 6 and int > 3:
            return "MEDIOCRE"
        if int < 10 and int > 6:
            return "GOOD"
        if int < 15 and int > 20:
            return "PERFECT"
        if int == 20:
            return "MASTERED"

    def getSkill(self, skill):
        return self.skills[skill]

    def getStrTalent(self, talent):
        talentInt = self.talents[talent]
        return self.scaleTalent(talentInt)

    def getIntTalent(self, talent):
        talentInt = self.talents[talent]
        return talentInt

    def getSkills(self):
        return self.skills

    def getTalents(self):
        return self.talents


class PlayerInventory:
    def __init__(self):
        self.slotCounter = 0
        self.newSlotCounter = 0
        self.emptySlot = False

        self.extras = {"goldCoins": 0}

        self.InvStats = {"maxCapacity": 10, "slots": self.slotCounter}
        self.EquippedItems = {"Right Hand": "Empty", "Left Hand": "Empty"}
        self.EquippedArmour = {
            "Head": "Empty",
            "Chest": "Empty",
            "Legs": "Empty",
            "Feet": "Empty",
        }
        self.Inventory = {}

    def getSlot(self, slot_number):
        if f"slot{slot_number}" in self.Inventory:
            return self.Inventory[f"slot{slot_number}"]
        else:
            return None

    def storeItem(self, item):
        """Stores an item value in the next available free item slot"""
        inventory = self.Inventory

        if self.slotCounter > self.InvStats["maxCapacity"]:
            return False
        else:
            item_id = item.getID()
            for slot_name, slot_item in inventory.items():
                if slot_item is not None and slot_item["itemID"] == item_id:
                    print("stacked items")
                    slot_item["itemCount"] += 1
                    return False

            if self.emptySlot == True:
                val = self.newSlotCounter
                inventory[f"slot{self.newSlotCounter}"] = item.addInv(
                    self.newSlotCounter
                )

                self.newSlotCounter = None
                self.emptySlot = False

                return True
            elif self.emptySlot == False:
                self.slotCounter += 1
                inventory[f"slot{self.slotCounter}"] = item.addInv(
                    self.slotCounter)

                return True

    def removeItem(self, slot):
        """Removes an item in the corresponding slot"""

        inventory = self.Inventory
        item = inventory[f"slot{slot}"]

        if item == None:  # Check if item exists
            return "Slot doesn't exist or is empty"  # Return if it doesn't
        elif (
            self.slotCounter == 0 or None
        ):  # Check if there are any items in the inventory
            return "Slot doesn't exist or is empty"  # Return if there isn't
        else:  # Else run the rest of the code to remove the item
            self.newSlotCounter = int(
                item["slot"]
            )  # changes to the value of the removed item
            # Changes for addItem(self) function validation
            self.emptySlot = True

            # removes the desired item from the dictionary
            inventory.pop(f"slot{slot}")
            item["memLocation"].removeInv()  # changes the item slot

            return f"Removed item in slot{slot}"

    def checkSpace(self):
        """Checks if the player has space in inventory"""

        if self.slotCounter < 10:
            return True
        else:
            return False

    def getInventory(self):
        """Returns the inventory dictionary"""
        return self.Inventory

    def getInvStats(self):
        """Returns the InvStats dictionary"""
        return self.InvStats

    def getEquippedItems(self):
        """Returns the EquippedItems dictionary"""
        return self.EquippedItems

    def getEquippedArmour(self):
        """Returns the EquippedArmour dictionary"""
        return self.EquippedArmour

    def getAmountSlots(self):
        """Returns the number of slots that are taken up"""
        return self.InvStats["slots"]


class Body:
    def __init__(self, playerProperties, playerInventory):
        self.playerInventory = playerInventory  # Corrected usage
        self.playerProperties = playerProperties

        self.body = {
            "health": 100,
            "maxHealth": 100,
            "age": 15,
            "weight": 52,
            "height": 5.9,
            "mana": 100,
            "maxMana": 100,
            "stamina": 100,
            "maxStamina": 100,
        }

    def damage(self, amount):
        health = self.body["health"]
        maxHealth = self.body["health"]

        if health - amount > 0:
            health = 0
        else:
            health = health - amount

    def heal(self, amount):
        health = self.body["health"]
        maxHealth = self.body["health"]

        if health + amount > maxHealth:
            health = maxHealth
        else:
            health = health + amount

    def age(self, amount):
        age = self.body["age"]
        age + amount

    def getHealth(self):
        return self.body["health"]

    def getBody(self):
        return self.body

    def getPlayerInventory(self):
        return self.playerInventory

    def getPlayerProperties(self):
        return self.playerProperties


class Player:
    def __init__(self, body):
        self.name = randomName()
        self.body = body

    def isNPC(self):
        return False

    def getName(self):
        return self.name

    def getBody(self):
        return self.body
