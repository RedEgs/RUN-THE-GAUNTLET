from statemachine import StateMachine, State
from PlayerSystem import *
from NpcSystem import *
from AiSystem import *
from ItemSystem import *

import zope.event

redegs = InitPlayer()

enemyAI = AI()
enemy = InitNPC("Angry Spider", "Humanoid", 1, enemyAI)

dragonSlayer = Item("Dragon Slayer", "50", "Guts' famous sword", "weapon")


class CombatSystem(StateMachine):
    "Combat System for handling events"

    standby = State(initial=True)
    active = State()

    EnterCombat = (
        standby.to(active)
        | active.to(standby)
    )

    challenger = None
    # The object (player or npc) thats defending against the attack
    defender = None

    attacking = challenger  # The object that should can move

    npc = None
    player = None

    def combatLoop(self):
        npcHealth = self.npc.getBody().getHealth()
        playerHealth = self.npc.getBody().getHealth()

        while npcHealth > 0 or playerHealth > 0:
            if self.attacking == self.npc:
                print(self.npc.getAI().combatDecision())
                self.attacking = self.player
            else:
                playerChoice = input("what move ")
                self.attacking = self.npc

    def on_enter_active(self, challenger, defender):
        self.challenger = challenger
        self.defender = defender

        if challenger.isNPC():
            self.npc = self.challenger
            self.player = self.defender
        else:
            self.npc = self.defender
            self.player = self.challenger

        self.npc.getAI().cycle()  # Standby -> Active
        self.npc.getAI().cycle()  # Active -> Combat

        print("Entering Combat")
        self.combatLoop()


combatSystem = CombatSystem()

combatSystem.EnterCombat(enemy, redegs)
