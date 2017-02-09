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
###############################################

from DMT.GameData import DataManager


class HauntedDungeon():


    def newGame(self):
	# TODO(DL): add working new game functionality
	# From Jerry's example
        self.dm = DataManager()
        self.dm.loadNewGame()
	# while not end of game
	self.generateText()
	# get input
	# do action
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



""" MAIN """
if __name__ == "__main__":
    hd = HauntedDungeon()
    hd.runit()
