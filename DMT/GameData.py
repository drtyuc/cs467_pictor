########################################################
#  FILENAME : GameData.py
#
#  DESCRIPTION : 
#      Reads the Haunted Dungeon's core text file(s)
#      into class instances and implements an API
#      for accessing and modifying the attributes of
#      of the class instances.
#
#  NOTES :
#      This file has beed tested for basic functionally,
#      however rigorous unit testing remains to be done. 
#      Missing 'LoadSavedGame' and 'SaveGame' methods
#  
#  AUTHOR : Jerry Hayes        START DATE : 01/27/2017
#
#  CHANGES :
# 
#  VERSION     DATE      WHO        DETAIL
#    0.1    01/27/2017   JH    Initial Beta Version
########################################################
import json

PRIMITIVE_FILENAME = 'data/primitives.json'

#Used to load class instance using a dedicated json file
class Filename():
	def __init__(self, filename):
		self.__dict__ = json.loads(open(filename).read())
	
#Used to load class instance 		
class Data():
	def __init__(self, data):
		self.__dict__ = data

#Main class used to manage game data
class DataManager():

    def __init__(self):
		self.__players = []
		self.__bags = []
		self.__rooms = []
		self.__exits = []
		self.__objects = []
		self.__ghosts = []
	
	#----------------------- Load New Game -----------------------
    def loadNewGame(self):

        self.__primitives = json.loads(open(PRIMITIVE_FILENAME).read())
           
        for i in self.__primitives['players']:
            self.__players.append(Data(i))		
		
        for i in self.__primitives['bags']:
            self.__bags.append(Data(i))		
				
        for i in self.__primitives['rooms']:
            self.__rooms.append(Data(i))

        for i in self.__primitives['exits']:
            self.__exits.append(Data(i))
        
        for i in self.__primitives['objects']:
            self.__objects.append(Data(i))
        
        for i in self.__primitives['ghosts']:
			self.__ghosts.append(Data(i))
			
			
	#------------------ Player Methods ---------------------------		
    def getPlayerHealth(self):
		return self.__players[0].health
		
    def getPlayerLocation(self):
	    return self.__players[0].location
	    
    def isPlayerVisible(self):
	    return self.__players[0].visible
	    
    def setPlayerHealth(self, health):
		self.__players[0].health = health
	
    def setPlayerLocation(self, location):
		self.__players[0].location = location
		
    def setPlayerVisible(self, visible):
		self.__players[0].visible = visible
	
	
	#------------------- Inventory Methods ----------------------	
    def getInventoryCapacity(self):
		return self.__bags[0].capacity
	
    def getInventoryWeight(self):
		weight = 0
		for i in self.__bags[0].objects:
			index = self.getObjectIndex(i)
			if index >= 0:
			    weight += self.__objects[index].weight
		return weight
	
    def getInventoryObjects(self):
		return self.__bags[0].objects
	
    def isSpaceInInventory(self, name):
		index = self.getObjectIndex(name)
		if ((self.getInventoryCapacity() - self.getInventoryWeight() 
		   - self.__objects[index].weight) > 0):
			return True
		else:
			return False
		
    def addInventoryObject(self, name):
		self.__bags[0].objects.append(name)
	
    def removeInventoryObject(self, name):
	    self.__bags[0].objects.remove(name)
	  
	  
    #------------------- Room Methods ----------------------   
    def getRoomNames(self):
		rooms = []
		for i in self.__rooms:
			rooms.append(i.name)
		return rooms   
		
    def getRoomLongDescription(self):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		return self.__rooms[index].longDescription
		
    def getRoomShortDescription(self):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		return self.__rooms[index].shortDescription
		
    def isRoomDiscovered(self):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		return self.__rooms[index].discovered
		
    def setRoomDiscovered(self, status):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		self.__rooms[index].discovered = status
	
    def isRoomLighted(self):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		return self.__rooms[index].lighted
	
    def setRoomLighted(self, status):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		self.__rooms[index].lighted = status
		
    def getRoomObjects(self):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		return self.__rooms[index].objects
	
    def addRoomObject(self, name):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		self.__rooms[index].objects.append(name)
		
    def removeRoomObject(self, name):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		self.__rooms[index].objects.remove(name)
	
    def getRoomExits(self):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		return self.__rooms[index].exits
		
		
	#------------------- Exit Methods ----------------------  
    def getExitNames(self):
        exits = []
        for i in self.__exits:
			exits.append(i.name)
        return exits
	
    def getExitLongDescription(self, name):
		index = self.getExitIndex(name)
		return self.__exits[index].longDescription
		
    def getExitShortDescription(self, name):
		index = self.getExitIndex(name)
		return self.__exits[index].shortDescription
		
    def getExitDirection(self, name):
		index = self.getExitIndex(name)
		return self.__exits[index].direction
		
    def isExitVisible(self, name):
		index = self.getExitIndex(name)
		return self.__exits[index].visible
		
    def setExitVisible(self, name, status):
		index = self.getExitIndex(name)
		self.__exits[index].visible = status
		
    def isExitUnlocked(self, name):
		index = self.getExitIndex(name)
		return self.__exits[index].unlocked
	
    def setExitUnlocked(self, name, status):
		index = self.getExitIndex(name)
		self.__exits[index].unlocked = status
		
    def getKeyObject(self, name):
		index = self.getExitIndex(name)
		return self.__exits[index].keyObject
	
    def getToRoom(self, name):
		index = self.getExitIndex(name)
		return self.__exits[index].toRoom
		
		
    #------------------- Object Methods ----------------------  
    def getObjectNames(self):
        objects = []
        for i in self.__objects:
			objects.append(i.name)
        return objects

    def getObjectLongDescription(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].longDescription
	
    def getObjectShortDescription(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].shortDescription
	
    def getObjectWeight(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].weight
	
    def isObjectAcquirable(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].acquirable	
		
    def isObjectVisible(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].visible
		
    def isObjectInRoom(self, name):
		for i in self.getRoomObjects():
			if i == name:
				return True
		return False
	
    def isObjectInInventory(self, name):
		for i in self.getInventoryObjects():
			if i == name:
				return True
		return False
		
    def setObjectVisible(self, name, status):
		index = self.getObjectIndex(name)
		self.__objects[index].visible = status
	
    def getObjectHealthPoints(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].healthPoints
	
    def isObjectLighted(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].lighted
		
    def setObjectLighted(self, name, status):
		index = self.getObjectIndex(name)
		self.__objects[index].lighted = status
		
    def isObjectUnlocked(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].unlocked
		
    def setObjectUnlocked(self, name, status):
		index = self.getObjectIndex(name)
		self.__objects[index].unlocked = status
	
    def getObjectProtectionPoints(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].protectionPoints
		
    def isObjectEquipped(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].equipped
	
    def setObjectEquipped(self, name, status):
		index = self.getObjectIndex(name)
		self.__objects[index].equipped = status
	
    def isObjectRead(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].read
	
    def setObjectRead(self, name, status):
		index = self.getObjectIndex(name)
		self.__objects[index].read = status
		
    def getObjectDamagePoints(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].damagePoints
	
	
	#------------------- Ghost Methods ---------------------- 
    def getGhostNames(self):
        ghosts = []
        for i in self.__ghosts:
			ghosts.append(i.name)
        return ghosts	
        
    def getGhostLongDescription(self, name):
		index = self.getGhostIndex(name)
		return self.__ghosts[index].longDescription
		
    def getGhostShortDescription(self, name):
		index = self.getGhostIndex(name)
		return self.__ghosts[index].shortDescription
	
    def isGhostVisible(self, name):
		index = self.getGhostIndex(name)
		return self.__ghosts[index].visible
		
    def setGhostVisible(self, name, status):
		index = self.getGhostIndex(name)
		self.__ghosts[index].visible = status
		
    def getGhostLocation(self, name):
		index = self.getGhostIndex(name)
		return self.__ghosts[index].location
		
    def setGhostLocation(self, name, location):
		index = self.getGhostIndex(name)
		self.__ghosts[index].location = location
		
    def getGhostHealth(self, name):
		index = self.getGhostIndex(name)
		return self.__ghosts[index].health
		
    def setGhostHealth(self, name, health):
		index = self.getGhostIndex(name)
		self.__ghosts[index].health = health
		
    def getGhostDamagePoints(self, name):
		index = self.getGhostIndex(name)
		return self.__ghosts[index].damagePoints	
		
			
		    
	#------------------- Index Methods ----------------------    
    def getObjectIndex(self, name):
		index = 0
		for i in self.__objects:
			if i.name == name:
				return index
			index += 1
		return -1 
	
    def getRoomIndex(self, name):
		index = 0
		for i in self.__rooms:
			if i.name == name:
				return index
			index += 1
		return -1 
		
    def getExitIndex(self, name):
		index = 0
		for i in self.__exits:
			if i.name == name:
				return index
			index += 1
		return -1
	
    def getGhostIndex(self,name):
		index = 0
		for i in self.__ghosts:
			if i.name == name:
				return index
			index += 1
		return -1
