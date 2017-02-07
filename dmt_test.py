"""#####################################################
   This file is intended as a short example of how to
   load and use the DataManager in the GameData.py module.
   
   TO BE DELETE BEFORE PROJECT SUBMISSION
   #####################################################"""
from DMT.GameData import DataManager

dm = DataManager()

#Loads primitive classes ...see unit test modules for specific examples
dm.loadNewGame()

#Loads command-dependency-action relationships
dep = dm.getDependencies()

#Print supported command tuples
for i in dep['commands']:
    print(i['tuple'])











