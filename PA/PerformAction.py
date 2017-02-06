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
	""" Gets first failed dependency hint """
	self.__hint = ""
	for dep in self.__dependencies:
	    cmd = "dm." + dep["method"]
	    if 'object' in dep:                        # If we have an object, insert it
	        index = cmd.find(')')
	        merge_object = cmd[:index] + "'" + dep["object"] + "'" + cmd[index:] 
	        cmd = merge_object
	    result = eval(cmd)
	    if result != dep["expect"]:
               self.__hint = dep["hint"]
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
	""" Return the hint for the failed dependency """
	return self.__hint


    def doCommandActions(self):
	""" BROKEN - Execute the action methods """
	# TODO(DL) - fix this and alter dm object
	for dep in self.__actions:
	    cmd = "self.dm." + dep["method"]
	    index = cmd.find(')')
	    if 'object' in dep and 'state' in dep:     # If we have an object, insert it
		if dep["state"] == True:
	            merge_object = cmd[:index] + "'" + dep["object"] + "', True"  + cmd[index:] 
		if dep["state"] == False:
	            merge_object = cmd[:index] + "'" + dep["object"] + "'"  + cmd[index:] 
	        cmd = merge_object
	    elif 'object' in dep:
	        merge_object = cmd[:index] + "'" + dep["object"] + "'" + cmd[index:] 
	        cmd = merge_object
	    elif 'state' in dep:
		if dep["state"] == True:
	            merge_object = cmd[:index] + "True"  + cmd[index:] 
	            cmd = merge_object
	    result = eval(cmd)
	    print cmd
	    print result
	return 


    def setGhostActions(self):
	""" triggers after player peforms one action """
	# TODO(DL): flesh out
	return 


""" using this so i can test functionality """
if __name__ == "__main__":
    dm = DataManager()
    dm.loadNewGame()
    print "Test go north"
    pa = PerformAction("go north", dm)
    print pa.areCommandDependenciesMet()
    print pa.getCommandDependenciesHint()
#    pa.doCommandActions()
    print "Test go west"
    pa2 = PerformAction("go west", dm)
    print pa2.areCommandDependenciesMet()
    print pa2.getCommandDependenciesHint()
#    pa2.doCommandActions()
