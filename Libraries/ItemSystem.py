import time

class Item:
    """
    A Class used for item types.  
    """       
    def __init__(self, name, weight, itemDesc, itemType): 
        self.name = name

        self.weight = weight
        self.itemDesc = itemDesc
        self.itemType = itemType

        self.slot = None
        self.itemCount = 1

        self.memLocation = self
        self.itemID = abs(hash(name))

        allowed_types = ["material", "item", "consumable", "weapon", "armour"]  # Define the allowed item types
        if self.itemType not in allowed_types:
            raise ValueError(f"Invalid itemType: {self.itemType}. It must be one of {allowed_types}")


    def getID(self):
        return self.itemID

    def getMetadata(self):
        """
        Returns all the data of the item as a dictionary
        {
            "name" : self.name,
            "weight" : self.weight,
            "itemDesc" : self.itemDesc,
            "itemType" : self.itemType,
            "slot" : self.slot,
            "itemCount" : self.itemCount,
            "memLocation" : self,
            "itemID" : self.itemID
        }

        """
        
        metadata = {
            "name" : self.name,
            "weight" : self.weight,
            "itemDesc" : self.itemDesc,
            "itemType" : self.itemType,
            "slot" : self.slot,
            "itemCount" : self.itemCount,
            "memLocation" : self,
            "itemID" : self.itemID
        }

        return metadata
    
    def checkInv(self):
        """
        Returns False if the item is not in an inventory. 
        Returns True if the item is in an inventory
        """
        if self.slot == None:
            return False
        else: return True

    def addInv(self, slotNum):
        """Used when the item is added to an inventory. Useless by itself"""
        self.slot = slotNum
        return self.getMetadata()

    def removeInv(self):
        """Used when an item is removed from an inventory. Uselss by itself"""
        self.slot = None
    
    def destroy(self):
        """Deletes the entire object reference completely"""
        del self

