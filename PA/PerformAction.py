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
###############################################
import json
import os.path
import sys

pathparent = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))
sys.path.insert(0, pathparent)

from DMT.GameData import DataManager


class PerformAction():


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


    def doCommandActions(self, dm):
	""" Execute the action methods return print success text """
	success = []
	for dep in self.__actions:
	    cmd = "dm." + dep["method"]
	    index = cmd.find(')')
	    merge_object = cmd[:index] + "'" + dep["object"] + "', " + str(dep["state"]) + cmd[index:] 
	    cmd = merge_object
	    result = eval(cmd)
	    if result:
		print result
	    print dep["text"]
	return 


    def setGhostActions(self):
	""" triggers after player peforms one action """
	# TODO(DL): flesh out
	# Each ghost will have a turn after the player has a turn
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
