###############################################
#   
#  FILENAME : PerformAction.py
#
#  DESCRIPTION : 
#      This is the module for performing actions.
#      Module will process a command, compare it
#      to a state dependency data structure to
#      find a best match. Associated dependency
#      methods are compared against anticipated
#      values. If all dependencies are met,
#      action methods are executed. Success text
#      is then sent back to the player. If
#      dependencies are not met, a hint is sent
#      to the player.
#
#  NOTES :
# 
#
#  AUTHOR : Daniel Loughlin START DATE : 02/05/2017
#
#  CHANGES :  Initial Version  
# 
#  VERSION     DATE      WHO        DETAIL
#    0.1    02/05/2017   DL    Initial Version
#    0.2    02/23/2017   DL    Support added for ghosts
###############################################
import json
import os.path
import sys
import random

pathparent = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))
sys.path.insert(0, pathparent)

from DMT.GameData import DataManager
import textwrap


class PerformAction():

    MAX_WIDTH = 70

    def __init__(self, command, dm):
	""" Constructor - need command & data manager object """
	self.__command = command                       # The command (eg. go north)
	self.__valid = self.__isCommandValid(dm)         # Is this a valid command
	if self.__valid:   		               # Get dependencies and actions
	    self.__getCommandDependenciesAndActions(dm)
	    self.__evalCommandDependenciesMet(dm)
	    self.__getCommandDependenciesHint(dm)


    def __isCommandValid(self, dm):
	""" Is the command valid """
        dep = dm.getDependencies()
	for cmd in dep["commands"]:
	    if self.__command == cmd["tuple"]:
		return True
	return False 


    def __getCommandDependenciesAndActions(self, dm):
	""" initializes list of dependency and action for object """
        dep = dm.getDependencies()
	for cmd in dep["commands"]:
	    if self.__command == cmd["tuple"]:
		self.__dependencies = cmd["dependencies"]
		self.__actions = cmd["actions"]
		break
	return 
  

    def __evalCommandDependenciesMet(self, dm):
	""" Answers the question are all dependencies met """
	self.__all_met = True
	for dep in self.__dependencies:
	    cmd = "dm." + dep["method"]
	    if 'object' in dep:                        # If we have an object, insert it
	        index = cmd.find(')')
	        merge_object = cmd[:index] + "'" + dep["object"] + "'" + cmd[index:] 
	        cmd = merge_object
	    result = eval(cmd)
	    if result != dep["expect"]:
               self.__all_met = False
	return


    def __getCommandDependenciesHint(self, dm):
        """ Gets first failed dependency hint and prints it """
        self.__hint = ""
        for dep in self.__dependencies:
            cmd = "dm." + dep["method"]
            if 'object' in dep:                        # If we have an object, insert it
                index = cmd.find(')')
                merge_object = cmd[:index] + "'" + dep["object"] + "'" + cmd[index:] 
                cmd = merge_object
            result = eval(cmd)
            if result != dep["expect"]:
                print ""
                print dep["hint"]
        return 


    def isCommandValid(self):
        """ Public is the command valid """
        return self.__valid


    def getCommand(self):
	""" Public return the command used to build PA object """
	return self.__command


    def areCommandDependenciesMet(self):
        """ Returns if all dependencies were met """
        return self.__all_met


    def getCommandDependenciesHint(self):
        """ Return the hint as a string for the failed dependency """
        return self.__hint

    def printIt(self, list):
        for element in list:
            print element

    def doCommandActions(self, dm):
        success = []
        for dep in self.__actions:
            cmd = "dm." + dep["method"]
            index = cmd.find(')')
            merge_object = cmd[:index] + "'" + dep["object"] + "', " + str(dep["state"]) + cmd[index:] 
            cmd = merge_object
            result = eval(cmd)
            if result:
                print ""
                lines = []
                for i in result.split('\n'):
                    lines += (textwrap.wrap(i, width=self.MAX_WIDTH, replace_whitespace=False))
                self.printIt(lines)
            if dep["text"]:
                print ""
                print dep["text"]
        return 


    def doGhostActions(self, dm):
	""" perform the ghost actions """
	for g in dm.getGhostNames():
	    if dm.getGhostHealth(g) < 1:
	        # if ghost has no health, skip
		continue
	    if dm.getGhostLocation(g) == dm.getPlayerLocation():
		if dm.isGhostVisible(g) == False:
		    # There's a chance the ghost will appear
		    self.__randomGhostVisible(g,dm)
		elif dm.isGhostVisible(g) == True:
		    # Attack if ghost is visible
		    self.__ghostAttacks(g,dm)
	    else:
		# move ghosts not in same room as player
		self.__randomMoveGhost(g, dm)
	return 


    def __randomMoveGhost(self, ghost, dm, r1=0, r2=10, r3=9):
	""" move a ghost to another room  """
	# r1 and r2 modify random range
	# r3 modifies chance ghost will move
	r = random.randint(r1,r2)
	if r >= r3:
            rooms = dm.getRoomNames()
            r = random.randint(0,(len(rooms)-1))
	    # move the ghost to the new room
            dm.setGhostLocation(ghost,rooms[r])
	return


    def __randomGhostVisible(self, ghost, dm, r1=0, r2=3, r3=1):
	""" randomly make a ghost visible """
	# r1 and r2 modify the random range
	# r3 sets the bar for the visibility chance
	r = random.randint(r1,r2)
	if r >= r3:
	    dm.setGhostVisible(ghost, True)
	return


    def __ghostAttacks(self, ghost, dm, r1=0, r2=20, r3=2, r4=1):
	""" ghost attack method """
	# r1 and r2 modify random range
	# r3 and r4 used to modify player protection expressions
        r = random.randint(r1,r2)
        # chance to hit gets reduced by players protection rating
        if r >= int(dm.getPlayerProtectionPoints() / r3) + r4:
            # if the ghost lands a blow, roll for damage
	    r = random.randint(0,dm.getGhostDamagePoints(ghost))
	    # if damage exceeds 0
	    if r > 0:
	        # damage is lessened by the player's protection points
	        health = dm.getPlayerHealth() - (r - (dm.getPlayerProtectionPoints() / r3))
	        dm.setPlayerHealth(health)
	        damageText = "FIGHT: " + ghost + " attacked you and reduced your health to " + str(health)
		print ""
		self.printIt(textwrap.wrap(damageText, width=self.MAX_WIDTH))
		# if the damage was 0
     	    else:
	        noDamageText = "FIGHT: " + ghost + " attacked you, but fails to inflict a wound!"
		print ""
		self.printIt(textwrap.wrap(noDamageText, width=self.MAX_WIDTH))
	    # if the ghost misses the player
	else:
	    missText = "FIGHT: " + ghost + " attempts an attack, but misses!"
	    print ""
	    self.printIt(textwrap.wrap(missText, width=self.MAX_WIDTH))
	return



""" using this so i can test functionality """
if __name__ == "__main__":
    dm = DataManager()
    dm.loadNewGame()
    print "Test go north"
    pa = PerformAction("go north", dm)
    print pa.areCommandDependenciesMet()
    print pa.getCommandDependenciesHint()
    print pa.doCommandActions(dm)
    print "Test go west"
    pa2 = PerformAction("go west", dm)
    print pa2.areCommandDependenciesMet()
    print pa2.getCommandDependenciesHint()
    print pa2.doCommandActions(dm)
