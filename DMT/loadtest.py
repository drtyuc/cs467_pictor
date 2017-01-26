"""
THIS FILE IS FOR CONCEPT DEMONSTRATION ONLY!!
"""
import json

#Load primary game data file into a json object
primitives = json.loads(open('primitives.json').read())
	
#Used to create a class instance from a json object 		
class Data():
	def __init__(self, data):
		self.__dict__ = data
		
#Create Rooms List (17 rooms)
rooms = []
for i in primitives['rooms']:
	rooms.append(Data(i))

#Create Exits List  (32 exits)
exits = []
for i in primitives['exits']:
	exits.append(Data(i))

#Create Object List (72 objects)
objects = []
for i in primitives['objects']:
	objects.append(Data(i))

# Create Ghost List  (4 ghosts)
ghosts = []
for i in primitives['ghosts']:
	ghosts.append(Data(i))


#Print all instance names
for i in rooms:
	print(i.name)

for i in exits:
	print(i.name)

for i in objects:
	print(i.name)

for i in ghosts:
	print(i.name)
	
