from cryptography.fernet import Fernet
import pygame
import os

pygame.init()
pygame.mixer.init()


class Audio:
    def load(self):
        sound_effects = {}
        for filename in os.listdir(self.soundEffectDir):
            # Adjust file extensions as needed
            if filename.endswith(".wav") or filename.endswith(".mp3"):
                # Remove the file extension
                sound_name = os.path.splitext(filename)[0]
                sound_path = os.path.join(self.soundEffectDir, filename)
                sound_effects[sound_name] = pygame.mixer.Sound(sound_path)
        return sound_effects

    def __init__(self):

        self.soundEffectDir = f"{os.getcwd()}/gameDat/soundEffects"
        self.soundEffects = self.load()

    def playSound(self, sound):
        sound_name = sound  # Replace with the actual name of the sound you want to play
        if sound_name in self.soundEffects:
            self.soundEffects[sound_name].play()


class Persistents:
    def __init__(self, saveName):
        import base64

        self.saveName = saveName
        self.savePath = f"{os.getcwd()}/{saveName}"

        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

        # Code for creating a save slot
        if os.path.isdir(str(self.saveName)):
            encFile = open(f"{self.savePath}\{self.saveName}.enc", "rb")
            self.key = encFile.read()
            encFile.close()
        else:
            print(os.mkdir(self.saveName))  # make a save slot

            encFile = open(f"{self.savePath}\{saveName}.enc", "wb")
            encFile.write(self.key)
            encFile.close()

        # End of code for creatisng a save slot

    def getEncKey(self):
        encFile = open(f"{self.savePath}\{self.saveName}.enc", "rb")
        self.key = encFile.read()
        encFile.close()

    def saveData(self, data, dataName):
        dataFile = open(f"{self.savePath}\{dataName}.dta", "ab")
        dataFile.write(self.fernet.encrypt(data.encode()))

        dataFile.close()

    def readData(self, dataName):
        dataFile = open(f"{self.savePath}\{dataName}.dta", "rb")
        data = dataFile.read()

        dataFile.close()
        return self.fernet.decrypt(data).decode()

# SECTION - Misc Functions


def fixName(self, name, num):
    currentChar = len(name)
    requiredSpace = num
    remainingSpace = requiredSpace - currentChar

    finalName = name + " " * remainingSpace

    return finalName


def extractInt(self, input_string):
    import re

    # Use regular expression to find the first number in the string
    match = re.search(r'\d+', input_string)

    if match:
        # Extract and return the matched number as an integer
        return int(match.group())
    else:
        # Return None if no number is found in the string
        return None
