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
	def __init__(self):

		self.__actionText = None 

		'''
		OBSOLETE CODE - will keep around for a second
		#the goal is to have a loader function to load these into the instance.....

		self.__roomList = ['ca', 'kt', 'sr', 'tr', 'pw', 'bh', 'tr', 'hw', 'wl', 'ap', 'ce', 'ct', 'ar', 'jl', 'cl', 'ot', 'bd', 'sq']

		self.__roomDescriptsLong = {
		'ca': 'You are in the common area.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'kt': 'You are in the kichen.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'sr': 'You are in the storeroom.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'tr': 'You are in the Treasure Room.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'pw': 'You are in the Passage Way.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'bh': 'You are in the Banquet Hall.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'hw': 'You are in the Hallway.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'wl': 'You are in the Wizard\'s Laboratory.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'ap': 'You are in the Alternate Plane.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'ce': 'You are in the Cave Entrance.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'ct': 'You are in the Closet.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'ar': 'You are in the Armory.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'jl': 'You are in the Jail.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'sr': 'You are in the Jail.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'cl': 'You are inside the Cell.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'ot': 'You are outside.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'bd': 'You are in the Bedroom.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'sq': 'You are in the Sleeping Quarters.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n'}



		self.__roomDescriptsShort = 
		{'ca': 'You are in the common area...', 
		'kt': 'You are in the kitchen...', 
		'sr': 'You are in the storeroom...',
		'tr': 'You are in the Treasure Room', 
		'pw': 'You are in the passage way...', 
		'bh': 'You are in the Banquet Hall...', 
		'hw': 'You are in the Hallway...', 
		'wl': 'You are in the Wizard\'s Laboratory', 
		'ap': 'You are in the Alternate Plane...',
		'ce':'You are looking at the Cave Entrance..', 
		'ct': 'You are back inside the Closet...', 
		'ar': 'You are in the Armory...', 
		'jl': 'You are back at the jail...',
		'cl':'You are inside the cell....', 
		'ot': 'You are outside!', 
		'bd': 'In the Bedroom', 
		'sq': 'You are in the sleeping quarters'}

		self.__exitDescript = {



		}
	
		'''



	'''
	Description: takes the roomLocation produced by a call to gameData's getPlayerLocation() 
	and returns the long description. This will normally be called within generateRoomDescription - see below. 

	'''

	def getLongRoomDescription():
		return self.roomDescriptionLong[roomLocation]


	'''
	Description: takes the roomLocation produced by a call to gameData's getPlayerLocation() and returns 
	the short description. This will normally be called within generateRoomDescription - see below. 

	'''

	def getShortRoomDescription(roomLocation):
		return self.roomDescriptsShort[roomLocation]

	'''
	Description: takes the roomLocation and whether it was vistied and then prints the roomDescription to console

	Ideally, this would accept the return values of gameData's getPlayerLocation() and isRoomDiscovered()

	'''
	def generateRoomDescription(self, roomLocation, visitedBool):

		if visitedBool:
			print getShortRoomDescription(roomLocation)
		else:
			print getRoomLongDescription[roomLocation]



if __name__ == '__main__':
	textDisplay()
