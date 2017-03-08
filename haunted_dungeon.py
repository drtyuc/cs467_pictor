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
#    0.4    02/21/2017   DL    added JH code and cleanedup 
###############################################

from DMT.GameData import DataManager
from commandNLP.nlp import nlp
from PA.PerformAction import PerformAction
import textwrap
import readline
import re


class HauntedDungeon():

    dm = DataManager()
    nlp = nlp()
    MAX_WIDTH = 70
    CLEAR_SCREEN = True  # Enables clearing of the screen after actions

    def playGame(self):
        """ haunted dungeon game play method loop """
        # setup nlp module prerequisites
        self.nlp.loadProperties(self.dm.getVerbs(), self.dm.getPrepositions(), self.dm.getObjects(), self.dm.getVerbPrepositionCombos(), self.dm.getExits(), self.dm.getCommandTuples())
        # print display text for current locale to player
        self.generateText()
        command = ""
        # compile the attack {object} regex for repeated use
        attackPattern = re.compile('(attack) (\w+)')
        # while not end of game
        while command != "quit":
            print ""
            command = raw_input("Your move: ")
	    if self.CLEAR_SCREEN == True:
	        print ("\n" * 100)  # clear screen..
            print ""
            print "-----------------------------------------------------------------------"
            # do action
            if command == "quit":
                print "GOOD BYE!"
                return
                
            """Temporary fix to NLP mapping problem
               Use buildTuple only when player input
               is not a supported command
            ***************************************"""
            if self.dm.isCommandTuple(command):
                commandTuple = command
            else:
                commandTuple = self.nlp.buildTuple(command)
                
            """ (temparary bypass) 
             commandTuple = self.nlp.buildTuple(command)
            **************************************"""

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
	""" show the main menu to the player and grab menu choice """
        choice = "" 
        while (choice != "1") and (choice != "2") and (choice != "3"):
            print "HAUNTED DUNGEON!!"
            print
            print "1) Start A New Game"
            print "2) Load A Saved Game"
            print "3) Exit"
            print
            choice = str(raw_input("Enter your choice> "))
	    if self.CLEAR_SCREEN == True:
	        print ("\n" * 100)  # clear screen.. 
            if choice == "1":
                self.loadNewGame()
            if choice == "2":
                choice = self.loadGame(choice)
            if choice == "3":
	        print "GOOD BYE!"
        return


    def runit(self):
	""" run the game """
	self.showMenu()
        return
    

    def formatList(self, list):
	""" assist with formatting text for display (eg. inventory) """
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
	""" assist with printing list structures (eg. game objects, inventory) """
	for element in list:
	    print element
	return



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
            self.printIt(textwrap.wrap("INVENTORY ITEMS: " + self.formatList(self.dm.getInventoryObjects()), self.MAX_WIDTH))
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
	            
        #Print ghosts
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
