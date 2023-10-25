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

    def combatDecision(self):
        if self.current_state == AI.combat:
            decision = random.randint(1, 4)
            if decision == 1:
                return "fireball"
            elif decision == 2:
                return "strike"
            elif decision == 3:
                return "dodge"
            elif decision == 4:
                return "stab"

        else:
            return "Not in Combat"
