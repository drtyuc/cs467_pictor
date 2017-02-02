		

class textDisplay():
	def __init__(self):

		self.roomList = ['CA', 'KT', 'SR', 'TR', 'PW', 'BH', 'TR', 'PW', 'BH', 'HA', 'WL', 'AP', 'CE', 'CO', 'AR', 'JA', 'CL', 'OU', 'BR', 'SQ']

		self.roomDescriptsLong = {'CA': 'You are in the common area.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'KT': 'You are in the kichen.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n',
		'SR': 'You are in the storeroom.\n\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac viverra nunc. Phasellus quam orci, dapibus venenatis risus sit amet, semper fringilla risus. Morbi lacinia nisl dolor, id dapibus tortor eleifend quis. Nunc sagittis gravida semper. Curabitur vulputate odio pretium ligula tincidunt tincidunt. Curabitur eu tempus justo. Suspendisse efficitur pharetra euismod. Quisque nec fringilla est. Nulla fermentum mollis auctor. Mauris varius suscipit scelerisque. Ut eu arcu sed eros aliquam pharetra. Phasellus et diam justo. Quisque vitae dui sit amet nibh varius rutrum eget sit amet est. Aliquam hendrerit eget augue lacinia mattis. Pellentesque dapibus fermentum massa.\n'}

		self.roomDescriptsShort = {'CA': 'You are in the common area...', 'KT': 'You are in the kitchen...', 'SR': 'You are in the storeroom...',
		'TR': 'You are in the Treasure Room', 'PW': 'You are in the passage way...', 'BH': 'You are in the Banquet Hall...', 
		'HA': 'You are in the Hallway...', 'WL': 'You are in the Wizard\'s Laboratory', 'AP': 'You are in the Alternate Plane...',
		'CE':'You are looking at the Cave Entrance..', 'CO': 'You are back inside the Closet...', 'AR': 'You are in the Armory...', 'JA': 'You are back at the jail...',
		'CL':'You are inside the cell....', 'OU': 'You are outside!', 'BR': 'In the Bedroom', 'SQ': 'You are in the sleeping quarters'}


	def generateRoomDescription(self, roomLocation, visitedBool):

		if visitedBool:
			print self.roomDescriptsShort[roomLocation]
		else:
			print self.roomDescriptsLong[roomLocation]


if __name__ == '__main__':
	td = textDisplay()

	for x in range(3):
		td.generateRoomDescription(td.roomList[x], False)
