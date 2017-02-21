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
from PA.PerformAction import PerformAction


class HauntedDungeon():

    dm = DataManager()

    def newGame1(self):
        # TODO(DL): functionality lacks nlp.py
        # This just has simple input grabbing
        #(JH) self.dm = DataManager()  Move this as a class attribute
        self.dm.loadNewGame()
        # while not end of game
        # print display text for current locale to player
        #(JH) self.generateText()
        self.generateText1()
        # basic input until we can get nlp to work
        command = ""
        while command != "quit":
            command = raw_input("Your move: ")
            # do action
            if command == "quit":
                print "GOOD BYE!"
                return
            pa = PerformAction(command, self.dm)
            if pa.isCommandValid() == True:
                if pa.areCommandDependenciesMet() == False:
                    pa.getCommandDependenciesHint()
                else:
                    pa.doCommandActions(self.dm)
            else:
                print "You can't do that!"
            #(JH)self.generateText()
            self.generateText1()
        return


    def newGame(self):
        # (DL): This is broken when I use nlp.py
        # right now it just prints the command if successful 
        self.dm = DataManager()
        self.dm.loadNewGame()
        self.nlp = nlp()
        self.nlp.loadProperties(self.dm.getVerbs(), self.dm.getPrepositions(), self.dm.getObjects(), self.dm.getVerbPrepositionCombos(), self.dm.getExits(), self.dm.getCommandTuples())
        self.nlp.buildSynonymDict()
        # while not end of game
        # print display text for current locale to player
        self.generateText()
        command = ""
        while command != "quit":
            command = raw_input("Your move: ")
            # do action
            if command == "quit":
                print "GOOD BYE!"
                return
            else:
                commandTuple = self.nlp.matchTuple(command)
                print "***CommandTuple is " 
                print commandTuple 
                if not any(commandTuple):
                    print "I don't understand..."

            pa = PerformAction(commandTuple, self.dm)
            if pa.isCommandValid() == True:
                if pa.areCommandDependenciesMet() == False:
                    pa.getCommandDependenciesHint()
                else:
                    pa.doCommandActions(self.dm)
            else:
                print "You can't do that!"
            #(JH)self.generateText()
            self.generateText1()
        return
 


    def loadGame(self):
	# TODO(DL): add load game functionality
        return

    
    def showMenu(self):
        choice = "" 
        while (choice != "1") and (choice != "2") and (choice != "3"):
            print "HAUNTED DUNGEON!!"
            print
            print "1) Start A New Game"
            print "2) Load A New Game"
            print "3) Exit"
            print
            choice = str(raw_input("Enter your choice> "))
        if choice == "1":
       	    #(JH) self.newGame()   
            self.newGame()
        if choice == "2":
            self.loadGame()
        return


    def runit(self):
	self.showMenu()

    '''
    Description: This function will generate the first portion for the display text for the game:
    the room description, the objects available, the exits, and any ghosts that are already visible

    '''
    def generateText(self):

        #print header info

        print
        print "Haunted Dungeon\t\t\t", "Health: " , self.dm.getPlayerHealth()

        if self.dm.isRoomDiscovered() == False:
            #print appropriate room description

            print self.dm.getRoomLongDescription()

            #get the objects in the room and print the visible ones 

            objectsAvailable = self.dm.getRoomObjects()

            print "You see these items..."

            for item in objectsAvailable:
                if self.dm.isObjectVisible(item):
                    print "*", item 

            #get the room exits and print the visible 
            print "You see these exits..."
            roomExits = self.dm.getRoomExits()

            for exit in roomExits:
                if self.dm.isExitVisible(exit):
                    print "To the " + self.dm.getExitDirection(exit), "..." + self.dm.getExitLongDescription(exit)

        else:
            print self.dm.getRoomShortDescription()
            objectsAvailable = self.dm.getRoomObjects()

            print "You see these items..."

            for item in objectsAvailable:
                if self.dm.isObjectVisible(item):
                    print "*", item 

            print "You see these exits..."
            roomExits = self.dm.getRoomExits()

            for exit in roomExits:
                if self.dm.isExitVisible(exit):
                    print "To the " + self.dm.getExitDirection(exit), "..." + self.dm.getExitShortDescription(exit)

        ghosts = self.dm.getGhostNames()

        for g in ghosts:
            if self.dm.getGhostLocation(g) == self.dm.getPlayerLocation():
                if self.dm.isGhostVisible(g):
                    print "You see " + self.dm.getGhostShortDescription(g) 


    #(JH) Added this as a temporary method for instructor cheat sheet
    def generateText1(self):

        #print header info

        print
        print "Health: " , self.dm.getPlayerHealth()
        
        #Print inventory
        if self.dm.getInventoryObjects():
            print "Inventory Capacity: " , self.dm.getInventoryCapacity()
            print "Inventory Weight: " , self.dm.getInventoryWeight()
            items = []
            for i in self.dm.getInventoryObjects():
                items.append(i)
            print "Invertory items: " + str(items)
                
        #Print equipped items
        if self.dm.getEquippedObjects():
            equipped = []
            for i in self.dm.getEquippedObjects():
                equipped.append(i)
            print "Equipped items: " + str(equipped)
            
        
        #Print room items
        if self.dm.getRoomObjects():
            roomitems = []
            for i in self.dm.getRoomObjects():
                roomitems.append(i)
            print "Room items: " + str(roomitems)
        
        #Print room and exit descriptions
        roomExits = self.dm.getRoomExits()
        if self.dm.isRoomDiscovered() == False: 
            print "Room: ", self.dm.getRoomLongDescription()
            for i in roomExits:
                if self.dm.isExitVisible(i):
                    print "Exit:  " +  self.dm.getExitLongDescription(i) + " to the " + self.dm.getExitDirection(i)
        else:
            print "Room: ", self.dm.getRoomShortDescription()
            for i in roomExits:
                if self.dm.isExitVisible(i):
                    print "Exit:  " +  self.dm.getExitShortDescription(i) + " to the " + self.dm.getExitDirection(i)
        self.dm.setRoomDiscovered(True) 
        
        
        #Print visible objects
        if self.dm.getVisibleObjects():
            print "You see these items..."
            for item in self.dm.getVisibleObjects():
                print "*", item
        else:
            print "You do not see any items"




""" MAIN """
if __name__ == "__main__":
    hd = HauntedDungeon()
    hd.runit()
