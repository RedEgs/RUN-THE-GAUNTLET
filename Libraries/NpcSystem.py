

def InitNPC(name, type, difficulty, AI):
    npcProp = NPCproperties()
    body = NPCbody(npcProp)
    npc = NPC(name, body, type, difficulty, AI)

    return npc


class NPC():
    def __init__(self, name, NPCbody, type, difficulty, AI):
        self.name = name
        self.NPCbody = NPCbody
        self.type = type
        self.difficulty = difficulty
        self.AI = AI

        allowedTypes = ["Humanoid", "Aggressive"]
        if self.type not in allowedTypes:
            raise ValueError(
                f"Invalid itemType: {self.type}. It must be one of {allowedTypes}")

    def isNPC(self):
        return True

    def getAI(self):
        return self.AI

    def getName(self):
        return self.name

    def getBody(self):
        return self.NPCbody

    def getType(self):
        return self.type


class NPCbody():
    def __init__(self, NPCproperties):
        self.NPCproperties = NPCproperties
        self.NPCbody = {
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
        health = self.NPCbody["health"]
        maxHealth = self.NPCbody["health"]

        if health - amount > 0:
            health = 0
        else:
            health = health - amount

    def heal(self, amount):
        health = self.NPCbody["health"]
        maxHealth = self.NPCbody["health"]

        if health + amount > maxHealth:
            health = maxHealth
        else:
            health = health + amount

    def age(self, amount):
        age = self.NPCbody["age"]
        age + amount

    def getHealth(self):
        return self.NPCbody["health"]

    def getBody(self):
        return self.NPCbody

    def getNPCproperties(self):
        return self.NPCproperties


class NPCproperties():
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
