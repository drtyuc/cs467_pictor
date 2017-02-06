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
	self.__dm = dm                                 # add the singleton game dm object as an attr for ease of access
	self.__valid = self.__isCommandValid()         # Is this a valid command
	if self.__valid:   		               # Get dependencies and actions
	    self.__getCommandDependenciesAndActions()


    def __isCommandValid(self):
	""" Is the command valid """
        dep = self.__dm.getDependencies()
	for cmd in dep["commands"]:
	    if self.__command == cmd["tuple"]:
		return True
	return False 


    def __getCommandDependenciesAndActions(self):
	""" initializes list of dependency and action for object """
        dep = self.__dm.getDependencies()
	for cmd in dep["commands"]:
	    if self.__command == cmd["tuple"]:
		self.__dependencies = cmd["dependencies"]
		self.__actions = cmd["actions"]
		break
	return 
  

    def isCommandValid(self):
	""" Public is the command valid """
	return self.__valid


    def getCommand(self):
	""" Public return the command used to build PA object """
	return self.__command


    def areCommandDependenciesMet(self):
	""" Answers the question are all dependencies met """
	# TODO(DL): WIP flesh out trying to figure out how to craft the method and evaluate it
	for dep in self.__dependencies:
	    print dep["method"]
	    #cmd = "self.__dm." + dep["method"]
	    #index = cmd.find(')')
	    #merge_object = cmd[:index] + "'" + dep["object"] + "'" + cmd[index:] 
	    #cmd = merge_object
	    #print cmd
	    #result = eval(cmd)
	    #print result
	return 


    def getCommandDependenciesHint(self):
	""" Gets first failed dependency hint """
	# TODO(DL): flesh out
	return 


    def getCommandActions(self):
	""" gets list of action methods and params """
	# TODO(DL): flesh out
	return 


    def doCommandActions(self):
	""" Execute the action methods """
	# TODO(DL): flesh out
	return 


    def setGhostActions(self):
	""" triggers after player peforms one action """
	# TODO(DL): flesh out
	return 


if __name__ == "__main__":
    dm = DataManager()
    dm.loadNewGame()
    pa = PerformAction("go north", dm)
    pa.areCommandDependenciesMet()
