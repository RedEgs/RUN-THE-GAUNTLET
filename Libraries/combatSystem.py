from typing import Any
from statemachine import StateMachine, State
from PlayerSystem import *
from NpcSystem import *
from AiSystem import *
from ItemSystem import *
from FightSystem import *

redegs = InitPlayer()


enemyAI = AI()
enemy = InitNPC("Angry Spider", "Humanoid", 1, enemyAI)

tinySwing = MeleeAttack("Tiny Swing", "A Tiny Swing", 10)
smallSwing = MeleeAttack("Small Swing", "A Small Swing", 20)
regularSwing = MeleeAttack("Regular Swing", "A Regular Swing", 50)
hugeSwing = MeleeAttack("Huge Swing", "A Huge Swing", 80)
massiveSwing = MeleeAttack("Huge Swing", "A Huge Swing", 120)

enemy.getBody().getNPCarsenal().equip_move(tinySwing)
enemy.getBody().getNPCarsenal().equip_move(smallSwing)
enemy.getBody().getNPCarsenal().equip_move(regularSwing)
enemy.getBody().getNPCarsenal().equip_move(hugeSwing)

redegs.getBody().getPlayerArsenal().equip_move(tinySwing)
redegs.getBody().getPlayerArsenal().equip_move(smallSwing)
redegs.getBody().getPlayerArsenal().equip_move(hugeSwing)
redegs.getBody().getPlayerArsenal().equip_move(massiveSwing)


class CombatSystem(StateMachine):
    "Combat System for handling events"

    standby = State(initial=True)
    active = State()

    EnterCombat = (
        standby.to(active)
        | active.to(standby)
    )

    attacking = None

    npc = None
    player = None

    def damageFighter(self, health, damage):
        health -= damage
        return health

    def combatLoop(self):
        npcHealth = self.npc.getBody().body["health"]
        playerHealth = self.player.getBody().body["health"]

        while playerHealth >= 0 and npcHealth >= 0:  # While the Player and NPC are still alive
            if self.npc == self.attacking:
                npcMove = self.npc.getAI().combatDecision(
                    self.npc.getBody().getNPCarsenal())  # Returns the NPC attack
                playerHealth = self.damageFighter(playerHealth, npcMove)

                self.attacking = self.player  # Switch the turn
            else:
                playerChoice = int(input("Your Move"))  # ask for input
                playerMove = self.player.getBody().getPlayerArsenal().useMove(playerChoice)
                npcHealth = self.damageFighter(npcHealth, playerMove)

                self.attacking = self.npc  # Switch the turn

        else:
            print(f"npcHealth: {npcHealth} | playerHealth: {playerHealth}")

    def on_enter_active(self, challenger, defender):
        if challenger.isNPC():
            self.npc = challenger
            self.player = defender
            self.attacking = self.npc
        else:
            self.player = challenger
            self.npc = defender
            self.attacking = self.player

        self.npc.getAI().cycle()  # Standby -> Active
        self.npc.getAI().cycle()  # Active -> Combat

        self.combatLoop()


combatSystem = CombatSystem()

combatSystem.EnterCombat(enemy, redegs)
