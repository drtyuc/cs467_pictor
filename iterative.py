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
from PA.PerformAction import PerformAction
from DMT.NLP import NLP
import textwrap
import readline
import re


class HauntedDungeon():

    dm = DataManager()
    nlp = NLP()
    MAX_WIDTH = 70

    def playGame(self):
        self.generateText()
        command = ""
        # compile the attack {object} regex for repeated use
        attackPattern = re.compile('(attack) (\w+)')
        
        while command != "quit":
            print ""
            command = raw_input("Your move: ")
            # do action
            
            print ""
            print "-----------------------------------------------------------------------"
            if command == "quit":
                print "GOOD BYE!"
                return
            commandTuple = self.nlp.getCommandMatch(command.lower(), "iterative")
            pa = PerformAction(commandTuple, self.dm)
            if pa.isCommandValid() == True:
                if pa.areCommandDependenciesMet() == False:
                    pa.getCommandDependenciesHint()
                else:
                    pa.doCommandActions(self.dm)
                    if attackPattern.match(commandTuple):
                        m = attackPattern.match(commandTuple)
                        pa.attackGhost(m.group(2), self.dm)
            else:
                print ""
                print "HINT:  You can't " + command + "!"
            pa.doGhostActions(self.dm)
            self.generateText()
        return


    def loadGame(self, choice):
	""" load a saved game """
        if self.dm.loadSavedGame():
            self.playGame()
            return choice
        else:
            return 0

    
    def loadNewGame(self):
	""" load a new game """
	self.dm.loadNewGame()
	self.playGame()
        return


    def showMenu(self):
        choice = "" 
        while (choice != "1") and (choice != "2") and (choice != "3"):
            print "HAUNTED DUNGEON!!"
            print
            print "1) Start A New Game"
            print "2) Load A Saved Game"
            print "3) Exit"
            print
            choice = str(raw_input("Enter your choice> "))
            if choice == "1":
                self.loadNewGame()
            if choice == "2":
                choice = self.loadGame(choice)
        return


    def runit(self):
	self.showMenu()


    def formatList(self, list):
        s = "[ "
        count = len(list)
        item = 0
        for i in list:
            item += 1
            if item == count:
                s += i
            else:
                s += i + ", "
        return s + " ]"

    def printIt(self, list):
        for element in list:
            print element


    def generateText(self):

        #print header info

        print ""
        print "-----------------------------------------------------------------------"
        print "HEALTH: " + str(self.dm.getPlayerHealth())
        print "PROTECTION: " + str(self.dm.getPlayerProtectionPoints())
        if self.dm.getEquippedWeapon():
            print "EQUIPPED WEAPON: " + str(self.dm.getEquippedWeapon()) + "   DAMAGE POTENTIAL: " + str(self.dm.getObjectDamagePoints(self.dm.getEquippedWeapon()))
        
        #Print inventory
        if self.dm.getInventoryObjects():
            print ""
            print "INVENTORY CAPACITY: " , self.dm.getInventoryCapacity()
            print "INVENTORY WEIGHT: " , self.dm.getInventoryWeight()
            self.printIt(textwrap.wrap("INVENTORTY ITEMS: " + self.formatList(self.dm.getInventoryObjects()), self.MAX_WIDTH))
            if self.dm.getEquippedObjects():
                self.printIt(textwrap.wrap("EQUIPPED ITEMS: " + self.formatList(self.dm.getEquippedObjects()), width=self.MAX_WIDTH))    
    
       
        #Print room and exit descriptions
        print ""
        roomExits = self.dm.getRoomExits()
        if self.dm.isRoomDiscovered() == False: 
            self.printIt(textwrap.wrap("ROOM: " + self.dm.getRoomLongDescription(), width=self.MAX_WIDTH))
            for i in roomExits:
                if self.dm.isExitVisible(i):
                    print ""
                    self.printIt(textwrap.wrap("EXIT: " +  self.dm.getExitLongDescription(i) , width=self.MAX_WIDTH))
        else:
            self.printIt(textwrap.wrap("ROOM: " + self.dm.getRoomShortDescription(), width=self.MAX_WIDTH))
            for i in roomExits:
                if self.dm.isExitVisible(i):
                    self.printIt(textwrap.wrap("EXIT: " +  self.dm.getExitShortDescription(i) , width=self.MAX_WIDTH))
        self.dm.setRoomDiscovered(True) 
        
        
        #Print visible objects
        print ""
        if self.dm.getVisibleObjects():
            print "You see these items..."
            for item in self.dm.getVisibleObjects():
                print "*", item
        else:
            print "You do not see any items"
	            
        # TODO(DL): Flesh out Print ghosts
        ghosts = self.dm.getGhostNames()

        for g in ghosts:
            if self.dm.getGhostLocation(g) == self.dm.getPlayerLocation():
                if self.dm.isGhostVisible(g):
		    print ""
                    self.printIt(textwrap.wrap("OH NO!!! You see a ghost! It's " + self.dm.getGhostShortDescription(g), width=self.MAX_WIDTH)) 



""" MAIN """
if __name__ == "__main__":
    hd = HauntedDungeon()
    hd.runit()
