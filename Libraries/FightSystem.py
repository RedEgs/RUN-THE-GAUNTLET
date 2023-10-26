from PlayerSystem import *
from NpcSystem import *
from AiSystem import *
from ItemSystem import *


class Move:
    def __init__(self, name, description, moveType, damageType):
        self.name = name
        self.description = description
        self.damageType = damageType
        self.moveType = moveType

    def getDamageType(self):
        return self.damageType

    def getMoveType(self):
        return self.moveType

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description


# Different Attack Types


class MeleeAttack(Move):
    def __init__(self, name, description, damage=0, moveType="attack", damageType="melee"):
        super().__init__(name, description, moveType, damageType)
        self.damage = damage

        self.damageType = "melee"
        self.moveType = "attack"

    def getDamage(self):
        return self.damage


class RangeAttack(Move):
    def __init__(self, name, description,  damage=0, range=0, moveType="attack", damageType="range"):
        super().__init__(name, description, moveType, damageType)
        self.damage = damage
        self.range = range

        self.damageType = "range"
        self.moveType = "attack"

    def getDamage(self):
        return self.damage

    def getRange(self):
        return self.range


class SpellAttack(Move):
    def __init__(self, name, description, damage=0, manaCost=0, moveType="attack", damageType="spell"):
        super().__init__(name, description, moveType, damageType)
        self.damage = damage
        self.manaCost = manaCost

        self.damageType = "spell"
        self.moveType = "attack"

    def getDamage(self):
        return self.damage

    def getManaCost(self):
        return self.manaCost


class UltimateAttack(Move):
    def __init__(self, name, description, damage=0, cooldown=0, moveType="attack", damageType="ultimate"):
        super().__init__(name, description, moveType, damageType)
        self.damage = damage
        self.cooldown = cooldown

        self.damageType = "ultimate"
        self.moveType = "attack"

    def getDamage(self):
        return self.damage

    def getCooldown(self):
        return self.cooldown

# Different Defend Types


class MeleeDefend(Move):
    def __init__(self, name, description,  damageReduction=0, moveType="defend", damageType="melee"):
        super().__init__(name, description, moveType, damageType)
        self.damageReduction = damageReduction

        self.damageType = "melee"
        self.moveType = "defend"

    def getDamageReduction(self):
        return self.damageReduction


class RangedDefend(Move):
    def __init__(self, name, description, damageReduction=0, moveType="defend", damageType="ranged"):
        super().__init__(name, description, moveType, damageType)
        self.damageReduction = damageReduction

        self.damageType = "ranged"
        self.moveType = "defend"

    def getDamageReduction(self):
        return self.damageReduction


class SpellDefend(Move):
    def __init__(self, name, description, damageReduction=0, manaCost=0, moveType="defend", damageType="spell"):
        super().__init__(name, description, moveType, damageType)
        self.damageReduction = damageReduction
        self.manaCost = manaCost

        self.damageType = "spell"
        self.moveType = "defend"

    def getDamageReduction(self):
        return self.damageReduction

    def getManaCost(self):
        return self.manaCost

# Different Spell Types


class SpellHeal(Move):
    def __init__(self, name, description, healingAmount=0, manaCost=0, moveType="heal", damageType="spell"):
        super().__init__(name, description, moveType, damageType)
        self.healingAmount = healingAmount
        self.manaCost = manaCost

        self.damageType = "spell"
        self.moveType = "heal"

    def getHealingAmount(self):
        return self.healingAmount

    def getManaCost(self):
        return self.manaCost


class spellBuff(Move):
    def __init__(self, name, description, buff=None, manaCost=0, moveType="buff", damageType="spell"):
        super().__init__(name, description, moveType, damageType)
        self.buff = buff
        self.manaCost = manaCost

        self.damageType = "spell"
        self.moveType = "buff"

    def getBuff(self):
        return self.buff

    def getManaCost(self):
        return self.manaCost


class spellDebuff(Move):
    def __init__(self, name, description, debuff=None, manaCost=0, moveType="debuff", damageType="spell"):
        super().__init__(name, description, moveType, damageType)
        self.debuff = debuff
        self.manaCost = manaCost

        self.damageType = "spell"
        self.moveType = "debuff"

    def getDebuff(self):
        return self.debuff

    def getManaCost(self):
        return self.manaCost
