###############################################
#   
#  FILENAME : textDisplay.py
#
#  DESCRIPTION : 
#      This is the module for displaying the gameText.
#
#  NOTES :
# 
#
#  AUTHOR : Andrew Bagwell START DATE : 02/01/2017
#
#  CHANGES :  Initial Version  
# 
#  VERSION     DATE      WHO        DETAIL
#    0.1    02/01/2017   AB    Initial Version
#    0.2    02/06/2017 	 AB    Expansion of Functionality 
###############################################

from GameData import DataManager 
		

class textDisplay():

	'''

	This creates the object instance....I'm adding these other properties because I can use 
	setter methods to set these with the return value from game data APIs.

	'''

	def __init__(self):
		self.__roomLD = None
		self.__roomSD = None
		self.__playerHealth = None
		self.__actionText = None 


	'''
	
	Description: this accessor method returns the action text of the textDisplay instance...s

	'''

	def getActionText(self):
		return self.__actionText


	'''

	Description: This mutator method takes an external string and sets the actionText property to that string

	'''

	def setActionText(self, textPassed):

		self.__actionText = textPassed


	'''
	Description: This function will generate the display text for the game. 

	'''
	def generateText(self):

		dm = DataManager() #this won't be the same instance that is running in the game module, so this probably won't work

		#reset the actionText to None
		self.setActionText(None)

		#print header info

		print "Haunted Dungeon\t\t\t", "Health: " , dm.getPlayerHealth()

		if dm.isRoomDiscovered() == False:
			#print appropriate room description

			print dm.getRoomLongDescription()

			#get the objects in the room and print the visible ones 

			objectsAvailable = dm.getRoomObjects()

			print "You see these items..."

			for item in objects:
				if dm.isObjectVisible(item):
					print "*", item 

			#get the room exits and print the visible 
			print "You see these exits..."
			roomExits = dm.getRoomsExits()

			for exit in roomExits:
				if dm.isExitVisible(exit):
					print "To the " + dm.getExitDirection(exit), "..." + dm.getExitLongDescription(exit)

		else:
			print dm.getRoomShortDescription()
			objectsAvailable = dm.getRoomObjects()

			print "You see these items..."

			for item in objects:
				if dm.isObjectVisible(item):
					print "*", item 

			print "You see these exits..."
			roomExits = dm.getRoomsExits()

			for exit in roomExits:
				if dm.isExitVisible(exit):
					print "To the " + dm.getExitDirection(exit), "..." + dm.getExitShortDescription(exit)

		#This will only 

		ghosts = dm.getGhostsNames()

		for g in ghosts:
			if dm.getGhostLocation(g) == dm.getPlayerLocation():
				if dm.isGhostVisible(g):
					print "You see " + dm.getGhostShortDescription(g) 


	
if __name__ == '__main__':
	textDisplay()
