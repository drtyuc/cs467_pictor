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

from DMT.GameData import DataManager


class PerformAction():


    def __init__(self, command):
	""" Constructor """
	self.command = command


    def getCommandDependencies(self):
	""" returns list of dependency methods """
	# TODO(DL): flesh out
	return 
  

    def areCommandDependenciesMet(self):
	""" Answers are all dependencies met """
	# TODO(DL): flesh out
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


    def isCommandValid(self):
	""" Is the command valid """
	# TODO(DL): flesh out
	return 


    def setGhostActions(self):
	""" triggers after player peforms one action """
	# TODO(DL): flesh out
	return 
