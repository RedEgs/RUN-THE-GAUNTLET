import random

level1 = {
    "dungeon1": {
        "description" : """As you cautiously descend into the small, dimly lit cellar, 
                        the cold, stone walls seem to close in around you. The air is thick with the musty scent 
                        of age-old secrets, and the only source of illumination is a single torch sputtering
                        in a rusted wall sconce. Shelves line the room, their contents obscured by the gloom, 
                        hinting at forgotten treasures or ominous artifacts waiting to be uncovered.
                        """,
        "options" : None,
        },
    "dungeon2": {
        "description" : """This cramped chamber feels like a nightmarish cobweb-covered 
                        crypt. Sticky strands of silk hang from the ceiling like macabre decorations. 
                        The floor is a gruesome mosaic of bones, remnants of unfortunate adventurers who 
                        stumbled into this spider's lair. In one corner, a massive arachnid lurks, its 
                        multifaceted eyes fixated on you, guarding a grotesque nest of wriggling offspring.
                        """,
        "options" : None,
        }
    }


class Level:
    def __init__(self, map):
        self.map = map
        self.rows = len(map)
        self.columns = len(map[0])

        self.playerX, self.playerY = 0, 0

        
