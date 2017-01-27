"""#####################################################
   This file is intended as a short example of how to
   load and use the DataManager in the GameData.py module.
   
   TO BE DELETE BEFORE PROJECT SUBMISSION
   #####################################################"""
from DMT.GameData import DataManager

dm = DataManager()

dm.loadNewGame()

print(dm.getGhostNames())
print(dm.getGhostLongDescription("Blinky"))
print(dm.getGhostShortDescription("Blinky"))
print("Ghost visible")
print(dm.isGhostVisible("Blinky"))
dm.setGhostVisible("Blinky", True)
print(dm.isGhostVisible("Blinky"))
print("Ghost location")
print(dm.getGhostLocation("Blinky"))
dm.setGhostLocation("Blinky", "SR")
print(dm.getGhostLocation("Blinky"))
print("Ghost health")
print(dm.getGhostHealth("Blinky"))
dm.setGhostHealth("Blinky", 56)
print(dm.getGhostHealth("Blinky"))
print("Ghost damage points")
print(dm.getGhostDamagePoints("Blinky"))










