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
from DMT.PerformAction import PerformAction
import textwrap


class HauntedDungeon():

    dm = DataManager()
    MAX_WIDTH = 70

    def newGame(self):
        self.dm.loadNewGame()
        self.generateText()
        command = ""
        while command != "quit":
            print ""
            command = raw_input("Your move: ")
            # do action
            
            print ""
            print "-----------------------------------------------------------------------"
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
                print ""
                print "HINT:  You can't do that!"
            self.generateText()
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
        print "HEALTH: " , self.dm.getPlayerHealth()
        
        #Print inventory
        if self.dm.getInventoryObjects():
            print "INVENTORY CAPACITY: " , self.dm.getInventoryCapacity()
            print "INVENTORY WEIGHT: " , self.dm.getInventoryWeight()
            self.printIt(textwrap.wrap("INVENTORTY ITEMS: " + self.formatList(self.dm.getInventoryObjects()), self.MAX_WIDTH))
                
        #Print equipped items
        if self.dm.getEquippedObjects():
            self.printIt(textwrap.wrap("EQUIPPED ITEMS: " + self.formatList(self.dm.getEquippedObjects()), width=self.MAX_WIDTH))
        
        #Print room items
        if self.dm.getRoomObjects():
            self.printIt(textwrap.wrap("ROOM ITEMS: " + self.formatList(self.dm.getRoomObjects()), width=self.MAX_WIDTH))
        
        #Print room and exit descriptions
        roomExits = self.dm.getRoomExits()
        if self.dm.isRoomDiscovered() == False: 
            print ""
            self.printIt(textwrap.wrap("ROOM: " + self.dm.getRoomLongDescription(), width=self.MAX_WIDTH))
            for i in roomExits:
                if self.dm.isExitVisible(i):
                    print ""
                    self.printIt(textwrap.wrap("EXIT:  " +  self.dm.getExitLongDescription(i) , width=self.MAX_WIDTH))
        else:
            self.printIt(textwrap.wrap("ROOM: " + self.dm.getRoomShortDescription(), width=self.MAX_WIDTH))
            for i in roomExits:
                if self.dm.isExitVisible(i):
                    self.printIt(textwrap.wrap("EXIT:  " +  self.dm.getExitShortDescription(i) , width=self.MAX_WIDTH))
        self.dm.setRoomDiscovered(True) 
        
        
        #Print visible objects
        print ""
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
