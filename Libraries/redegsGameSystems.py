import pygame
import os

pygame.init()
pygame.mixer.init()


class Audio:
    def load(self):
        sound_effects = {}
        for filename in os.listdir(self.soundEffectDir):
            if filename.endswith(".wav") or filename.endswith(".mp3"):  # Adjust file extensions as needed
                sound_name = os.path.splitext(filename)[0]  # Remove the file extension
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

def findSave(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return True
