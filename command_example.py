#!/usr/bin/env python
###############################################
#   
#  Haunted Dungeon Game
#
#  By Team Pictor:
#      Andrew Bagwell
#      Jerry Hayes
#      Daniel Loughlin
#
#  OSU CS 467 Winter 2017
#
#  FILENAME : haunted_dungeon.py
#
#  DESCRIPTION : 
#      This is the main game file.
#
#  NOTES :
# 
#
#  AUTHOR : Daniel Loughlin START DATE : 02/05/2017
#
#  CHANGES :  Initial Version  
# 
#  VERSION     DATE      WHO        DETAIL
#    0.1    02/04/2017   DL    Initial Version
#    0.2    02/08/2017   AB    added generateText()
#    0.3    02/08/2017   DL    updated newGame()
###############################################

from DMT.GameData import DataManager
from commandNLP.nlp import nlp


class HauntedDungeon():
    
    dm = DataManager()
    dm.loadNewGame()
    dep = dm.getDependencies()
    
                
    def checkDependency(self, method, obj, expect):
        if method == 'isExitInRoom()':
            return self.dm.isExitInRoom(obj) == expect
        if method == 'isExitKeyInInventory()':
            return self.dm.isExitKeyInInventory(obj) == expect   
        if method == 'isExitUnlocked()':
            return self.dm.isExitUnlocked(obj) == expect 
        if method == 'isExitVisible()':
            return self.dm.isExitVisible(obj) == expect  
        if method == 'isLookAbovePossible()':
            return self.dm.isLookAbovePossible(obj) == expect   
        if method == 'isLookBehindPossible()':
            return self.dm.isLookBehindPossible(obj) == expect
        if method == 'isLookInsidePossible()':
            return self.dm.isLookInsidePossible(obj) == expect  
        if method == 'isLookOnPossible()':
            return self.dm.isLookOnPossible(obj) == expect 
        if method == 'isLookUnderPossible()':
            return self.dm.isLookUnderPossible(obj) == expect             
        if method == 'isObjectAccessible()':
            return self.dm.isObjectAccessible(obj) == expect 
        if method == 'isObjectAcquirable()':
            return self.dm.isObjectAcquirable(obj) == expect 
        if method == 'isObjectDrinkable()':
            return self.dm.isObjectDrinkable(obj) == expect         
        if method == 'isObjectEdible()':
            return self.dm.isObjectEdible(obj) == expect   
        if method == 'isObjectEquippable()':
            return self.dm.isObjectEquippable(obj) == expect          
        if method == 'isObjectEquipped()':
            return self.dm.isObjectEquipped(obj) == expect  
        if method == 'isObjectInInventory()':
            return self.dm.isObjectInInventory(obj) == expect
        if method == 'isObjectInRoom()':
            return self.dm.isObjectInRoom(obj) == expect 
        if method == 'isObjectKeyInInventory()':
            return self.dm.isObjectKeyInInventory(obj) == expect  
        if method == 'isObjectLayable()':
            return self.dm.isObjectLayable(obj) == expect 
        if method == 'isObjectLightable()':
            return self.dm.isObjectLightable(obj) == expect 
        if method == 'isObjectLighted()':
            return self.dm.isObjectLighted(obj) == expect      
        if method == 'isObjectPullable()':
            return self.dm.isObjectPullable(obj) == expect           
        if method == 'isObjectPushable()':
            return self.dm.isObjectPushable(obj) == expect     
        if method == 'isObjectRead()':
            return self.dm.isObjectRead(obj) == expect   
        if method == 'isObjectReadable()':
            return self.dm.isObjectReadable(obj) == expect      
        if method == 'isObjectSitable()':
            return self.dm.isObjectSitable(obj) == expect           
        if method == 'isObjectUnlocked()':
            return self.dm.isObjectUnlocked(obj) == expect   
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect    
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect
        if method == 'isSpaceInInventory()':
            return self.dm.isSpaceInInventory(obj) == expect  
        print("DEPENDENCY NOT SUPPORTED: " + method)
        return False
        
    def performAction(self, method, obj, state):
        if method == 'addInventoryObject()':
            self.dm.addInventoryObject(obj, state)
            return
        if method == 'addRoomObject()':
            self.dm.addRoomObject(obj, state)
            return
        if method == 'adjustGhostHealth()':
            self.dm.adjustGhostHealth(obj, state)
            return
        if method == 'adjustPlayerHealth()':
            self.dm.adjustPlayerHealth(obj, state) 
            return
        if method == 'changeLocation()':
            self.dm.changeLocation(obj, state)
            return
        if method == 'getObjectLongDescription()':
            self.dm.getObjectLongDescription(obj, state)
            return                
        if method == 'movePlayer()':
            self.dm.movePlayer(obj, state) 
            return   
        if method == 'removeInventoryObject()':
            self.dm.removeInventoryObject(obj, state) 
            return      
        if method == 'removeRoomObject()':
            self.dm.removeRoomObject(obj, state)
            return
        if method == 'setAboveObjectsVisible()':
            self.dm.setAboveObjectsVisible(obj, state)
            return
        if method == 'setBehindObjectsVisible()':
            self.dm.setBehindObjectsVisible(obj, state)
            return    
        if method == 'setExitUnlocked()':
            self.dm.setExitUnlocked(obj, state)  
            return 
        if method == 'setInsideObjectsVisible()':
            self.dm.setInsideObjectsVisible(obj, state)    
            return
        if method == 'setObjectEquipped()':
            self.dm.setObjectEquipped(obj, state)  
            return 
        if method == 'setObjectLighted()':
            self.dm.setObjectLighted(obj, state) 
            return   
        if method == 'setObjectRead()':
            self.dm.setObjectRead(obj, state)  
            return 
        if method == 'setObjectUnlocked()':
            self.dm.setObjectUnlocked(obj, state)
            return
        if method == 'setOnObjectsVisible()':
            self.dm.setOnObjectsVisible(obj, state)
            return 
        if method == 'setUnderObjectsVisible()':
            self.dm.setUnderObjectsVisible(obj, state) 
            return
        print("ACTION NOT SUPPORTED: " + method)
        return False    
    
    
    def getDependencyIndex(self, cmd):
        index = 0
        for i in self.dep['commands']:
            if i['tuple'] == cmd:
                return index
            index += 1
        return -1 
        
    def isCommandTuple(self, command):
        for i in self.dep['commands']:
            if command == i['tuple']:
                return True
        return False
    
    
            
    def command(self):
        command = raw_input("Please enter a command: ")
        if self.isCommandTuple(command):
            index = self.getDependencyIndex(command)
            d = self.dep['commands'][index]['dependencies']
            for i in range(len(d)):
                if not self.checkDependency(d[i]['method'], d[i]['object'], d[i]['expect']):
                    print(d[i]['hint'])
                    return "continue"   
            a = self.dep['commands'][index]['actions']
            for i in range(len(a)):
                self.performAction(a[i]['method'], a[i]['object'], a[i]['state'])
            print("success")
            return "continue"
        if command == 'quit':
            print("Good bye")
            return "quit"    
        print(command + " is not supported")
        return "continue"


    def displayInfo(self):
        print("")
        print("INFO    (type 'quit' to exit)"   )
        print("  Room: "+ self.dm.getCurrentRoom())
        for i in self.dm.getRoomExitDescriptions():
            print("  Room Exit: " + i)
        for j in self.dm.getRoomObjects():
            print("  Room Object: " + j)
        for j in self.dm.getVisibleObjects():
            print("  Visible Object: " + j)
        for k in self.dm.getInventoryObjects():
            print("  Inventory Object: " + k)
        print("  Player Health: " + str(self.dm.getPlayerHealth()))
        print("  Inventory Weight: " + str(self.dm.getInventoryWeight())) 
        print("")
            
            
    def showMenu(self):
        choice = "continue"
        while choice != "quit":
            self.displayInfo()
            choice = self.command()
        return


    def runit(self):
	self.showMenu()

   


if __name__ == "__main__":
    hd = HauntedDungeon()
    hd.runit()
