from statemachine import StateMachine, State
from NpcSystem import *
import random


class AI(StateMachine):
    "Brain of an NPC"

    standby = State(initial=True)
    active = State()
    combat = State()

    cycle = (
        standby.to(active)
        | active.to(combat)
        | combat.to(standby)
    )

    def before_cycle(self, event: str, source: State, target: State, message: str = ""):
        message = "." + message if message else ""
        return f"Changing AI {event} from {source.id} to {target.id}{message}"

    def on_enter_active(self):
        pass

    def on_enter_combat(self):
        print("AI Entering Combat Mode")

    def combatDecision(self, arsenal):

        if self.current_state == AI.combat:
            decision = random.randint(1, 4)
            if decision == 1:
                moveName, damage = arsenal.useMove(0)

                print(f"You were hit by {moveName} for {damage} damage!")
                return damage
            elif decision == 2:
                moveName, damage = arsenal.useMove(1)

                print(f"You were hit by {moveName} for {damage} damage!")
                return damage
            elif decision == 3:
                moveName, damage = arsenal.useMove(2)

                print(f"You were hit by {moveName} for {damage} damage!")
                return damage
            elif decision == 4:
                moveName, damage = arsenal.useMove(3)

                print(f"You were hit by {moveName} for {damage} damage!")
                return damage

        else:
            return "Not in Combat"
