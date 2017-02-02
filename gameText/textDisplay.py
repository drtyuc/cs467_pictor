
roomList = ['CA', 'KT', 'SR', 'TR', 'PW', 'BH', 'TR', 'PW', 'BH', 'HA', 'WL', 'AP', 'CE', 'CO', 'AR', 'JA', 'CL', 'OU', 'BR', 'SQ']

roomDescriptsLong = {'1': 'You are in the common area.'}

roomDescriptsShort = {'CA': 'You are in the common area...', 'KT': 'You are in the kitchen...', 'SR': 'You are in the storeroom...',
'TR': 'You are in the Treasure Room', 'PW': 'You are in the passage way...', 'BH': 'You are in the Banquet Hall...', 
'HA': 'You are in the Hallway...', 'WL': 'You are in the Wizard\'s Laboratory', 'AP': 'You are in the Alternate Plane...',
'CE':'You are looking at the Cave Entrance..', 'CO': 'You are back inside the Closet...', 'AR': 'You are in the Armory...', 'JA': 'You are back at the jail...',
'CL':'You are inside the cell....', 'OU': 'You are outside!', 'BR': 'In the Bedroom', 'SQ': 'You are in the sleeping quarters'}


def generateRoomDescription(roomLocation, visitedBool):

	if visitedBool:
		print roomDescriptsShort[roomLocation]
	else:
		print roomDescriptsLong[roomLocation]

def textDisplay():

	for x in range(len(roomList)):
		generateRoomDescription(roomList[x], True)


if __name__ == '__main__':
	textDisplay()
