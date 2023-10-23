def action1():
    print("returning home...")

def action2():
    print("running the gauntlet...")

interactionData = {
    "1": {  # 1
        "Choice": {
            "1": "Would you like to return home?",
            "action" : action1
        }
    },
    "2": {  # 2
        "Choice": {
            "2": "Would you like to run the gauntlet?",
            "action" : action2
        }
    },
    "3" : {
        "Dialogue": "Talk to OPERATOR",
        "Options" : {
            "1": {
                "option" : "How did I get here?",
                "response" : "You got teleported here."
            },
            "2": {
                "option" : "How do I leave?",
                "response" : "You can't."
            }
        }

    }
}


"""
=====================================
Welcome to the Lobby.

1. Would You Like to return home?
2. Would You Like to run the gauntlet?
3. Talk to OPERATOR

"""

"""
If Input == 1.:
    expand dialogue
elif Input == 2.:
    expand dialogue


"""

class Interaction:
    def __init__(self, interactionData):
        self.interactionData = interactionData

    def execute(self, action):
        if action is not None:
            action()

    def back(self):
        self.displayInteraction()

    def displayInteraction(self):
        numOptions = len(interactionData)  # Checks amount of available options

        for key, value in self.interactionData.items():
            if 'Choice' in value:

                choice_data = value['Choice']
                text = choice_data[key]
                print(f"{key}. {text}")

            elif 'Dialogue' in value:

                text = value['Dialogue']
                print(f"{key}. {text}")
        
        playerInput = str(input(">> "))
        for key2, value in self.interactionData.items():
            if 'Choice' in value:
                if key2 == playerInput:
                    action = value["Choice"]["action"]
                    self.execute(action)
                    break
            elif 'Dialogue' in value:
                if key2 == playerInput:
                    value = value["Options"]
                    for key3, option in value.items():
                        option = option["option"]
                        return(f"{key3}. {option}")
                    
                playerInput = str(input(">> "))
                for key4, option in value.items():
                    if key4 == playerInput:
                        response = option["response"]
                        return(response)
                        self.back()
            else:
                self.back()

         
