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
#      Missing 'LoadSavedGame' and SaveGame' methods
#  
#  CHANGES IN LATEST RELEASE
# 
#
#  AUTHOR : Jerry Hayes        START DATE : 01/27/2017
#
#  CHANGES :  Updated methods according to methods identified
#             in 'State Dependency Details' spreadsheet.  
# 
#  VERSION     DATE      WHO        DETAIL
#    0.1    01/27/2017   JH    Initial Beta Version
#    0.2    02/02/2017   JH    
########################################################
import json


PRIMITIVE_FILENAME = 'data/primitives.json'
DEPENDENCY_FILENAME = 'data/dependency_example.json'

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
			
    #----------------------- Print commands -----------------------
    def printCommands(self):

        self.commands = json.loads(open(DEPENDENCY_FILENAME).read())
           
           
        for i in self.commands['commands']:
            print i['tuple']
	
			
	#------------------ Player Methods ---------------------------		
    def getPlayerHealth(self):
		return self.__players[0].health
		
    def getPlayerLocation(self):
	    return self.__players[0].location
	    
    def isPlayerVisible(self):
	    return self.__players[0].visible
	    
    def adjustPlayerHealth(self, name):
		index = self.getObjectIndex(name)
		self.__players[0].health += self.__objects[index].healthPoints
	
    def setPlayerLocation(self, location):
		self.__players[0].location = location
		
    def setPlayerVisible(self, visible):
		self.__players[0].visible = visible
		
    def movePlayer(self, direction):
        index = self.getExitIndex(direction)
        self.__players[0].location = self.__exits[index].toRoom	
	
	#------------------- Inventory Methods ----------------------	
    def getInventoryCapacity(self):
		return self.__bags[0].capacity

    def setInventoryCapacity(self, capacity):
        self.__bags[0].capacity = capacity
	
    def getInventoryWeight(self):
		weight = 0
		for i in self.__bags[0].objects:
			index = self.getObjectIndex(i)
			if index >= 0:
			    weight += self.__objects[index].weight
		return weight
	
    def getInventoryObjects(self):
		return self.__bags[0].objects
	
    def clearInventoryObjects(self):
        self.__bags[0].objects = []

    def isSpaceInInventory(self, name):
		index = self.getObjectIndex(name)
		if ((self.getInventoryCapacity() - self.getInventoryWeight() 
		   - self.__objects[index].weight) > 0):
			return True
		else:
			return False

    def addInventoryObject(self, name):
        self.__bags[0].objects.append(name)
        index = self.getObjectIndex(name)
        self.__objects[index].location = "inventory"	
		
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
        oindex = self.getObjectIndex(name)
        self.__objects[oindex].location = location		
		
    def removeRoomObject(self, name):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		self.__rooms[index].objects.remove(name)
	
    def getRoomExits(self):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		return self.__rooms[index].exits
		
    def clearRoomObjects(self):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		self.__rooms[index].objects = []
		
		
	#------------------- Exit Methods ----------------------  
    def getExitNames(self):
        exits = []
        for i in self.__exits:
			exits.append(i.name)
        return exits
	
    def getExitLongDescription(self, name):
		index = self.getEindex(name)
		return self.__exits[index].longDescription	

    def getExitShortDescription(self, name):
		index = self.getExitIndex(name)
		return self.__exits[index].shortDescription
	
    def getExitDirection(self, name):
		index = self.getExitIndex(name)
		return self.__exits[index].direction
	
    def getExitKeyObject(self, name):
		index = self.getExitIndex(name)
		return self.__exits[index].keyObject
		
    def isExitVisible(self, name):
        index = self.getExitIndex(name)
        return self.__exits[index].visible
        
    def setExitVisible(self, name, status):
		index = self.getExitIndex(name)
		self.__exits[index].visible = status
		
    def isExitUnlocked(self, name):
        index = self.getExitIndex(name)
        return self.__exits[index].unlocked
        
    def isExitInRoom(self, name):
        index = self.getExitIndex(name)
        if self.__exits[index].name in self.getRoomExits():
            return True
        return False
        
    def isExitKeyInInventory(self, name):
        index = self.getExitIndex(name)
        if self.__exits[index].keyObject in self.__bags[0].objects:
            return True
        if self.__exits[index].keyObject == '':
            return True
        return False   
        
    def setExitUnlocked(self, name, status):
        index = self.getExitIndex(name)
        self.__exits[index].unlocked = status
        
    def getExitToRoom(self, name):
        index = self.getExitIndex(name)
        return self.__exits[index].toRoom
	

		
    #------------------- Object Methods ----------------------  
    def changeLocation(self, name):
        index = self.getObjectIndex(name)
        self.__players[0].location = self.__objects[index].keyObject	
    
    def isLookOnPossible(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].lookOn
    
    def isLookInsidePossible(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].lookInside
    
    def isLookAbovePossible(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].lookAbove
        
    def isLookUnderPossible(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].lookUnder
        
    def isLookBehindPossible(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].lookBehind
        
    def isObjectAccessible(self, name):
        return (isObjectInInventory(name) or isObjectInRoom(name))    
    		
    def isObjectAcquirable(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].acquirable		
	
    def isObjectDrinkable(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].drinkable
        
    def isObjectEdible(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].edible
        
    def isObjectEquippable(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].equippable
	
    def isObjectEquipped(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].equipped	
	
    def isObjectInInventory(self, name):
		for i in self.getInventoryObjects():
			if i == name:
				return True
		return False	
		
    def isObjectInRoom(self, name):
		for i in self.getRoomObjects():
			if i == name:
				return True
		return False	
		
    def isObjectKeyInInventory(self, name):
        index = self.getObjectIndex(name)
        if self.__objects[index].keyObject in self.__bags[0].objects:
            return True
        if self.__objects[index].keyObject == '':
            return True
        return False
        
    def isObjectLayable(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].layable		
		
    def isObjectLightable(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].lightable		
        
    def isObjectLighted(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].lighted     
		
    def isObjectLockable(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].lockable	
        
    def isObjectOpenable(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].openable	  
        
    def isObjectPickable(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].pickable	
	
    def isObjectPullable(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].pullable	
		
    def isObjectPushable(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].pushable			
        
    def isObjectRead(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].read        
        		
    def isObjectReadable(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].readable	

    def isObjectSitable(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].sitable	
       
    def isObjectUnlocked(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].unlocked        
        				
    def isObjectUseable(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].useable

    def isObjectVisible(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].visible
        
    def isObjectWieldable(self, name):
        index = self.getObjectIndex(name)
        return self.__objects[index].wieldable		
			 
    def getObjectLongDescription(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].longDescription
	
    def getObjectShortDescription(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].shortDescription   
        		
    def getObjectWeight(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].weight
		
    def getObjectHealthPoints(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].healthPoints	
	
    def getObjectDamagePoints(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].damagePoints	
		
    def getObjectProtectionPoints(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].protectionPoints	
		
    def getObjectKeyObject(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].keyObject		
		
    def getObjectLocation(self, name):
		index = self.getObjectIndex(name)
		return self.__objects[index].location

    def setObjectLocation(self, name, location):
		index = self.getObjectIndex(name)
		self.__objects[index].location = location	

    def setObjectVisible(self, name, status):
		index = self.getObjectIndex(name)
		self.__objects[index].visible = status			
			
    def setObjectLighted(self, name, status):
		index = self.getObjectIndex(name)
		self.__objects[index].lighted = status		
		
    def setObjectUnlocked(self, name, status):
		index = self.getObjectIndex(name)
		self.__objects[index].unlocked = status	
	
    def setObjectEquipped(self, name, status):
		index = self.getObjectIndex(name)
		self.__objects[index].equipped = status
	
    def setObjectRead(self, name, status):
		index = self.getObjectIndex(name)
		self.__objects[index].read = status

    def getObjectNames(self):
        objects = []
        for i in self.__objects:
			objects.append(i.name)
        return objects						
		
	# methods supporting look {on, inside, above, behind, under}	
    def setOnObjectsVisible(self, name, status):
        objects = self.getOnNames(name)
        for i in objects:
            index = self.getObjectIndex(i)
            self.__objects[index].visible = status
            
    def getOnObjectsVisible(self, name):
        objects = []
        for i in self.getOnNames(name):       
            index = self.getObjectIndex(i)
            if self.__objects[index].visible == True:
				objects.append(i)
        return objects
		    	    
    def getOnNames(self, name):
        objects = []
        for i in self.__objects:
            if (i.location == name) and (i.lookOn == True):
                objects.append(i.name)
        return objects

    def setInsideObjectsVisible(self, name, status):
        objects = self.getInsideNames(name)
        for i in objects:
            index = self.getObjectIndex(i)
            self.__objects[index].visible = status
            
    def getInsideObjectsVisible(self, name):
        objects = []
        for i in self.getInsideNames(name):       
            index = self.getObjectIndex(i)
            if self.__objects[index].visible == True:
				objects.append(i)
        return objects
		    	    
    def getInsideNames(self, name):
        objects = []
        for i in self.__objects:
            if (i.location == name) and (i.lookInside == True):
                objects.append(i.name)
        return objects
						
                        
    def setBehindObjectsVisible(self, name, status):
        objects = self.getBehindNames(name)
        for i in objects:
            index = self.getObjectIndex(i)
            self.__objects[index].visible = status
            
    def getBehindObjectsVisible(self, name):
        objects = []
        for i in self.getBehindNames(name):       
            index = self.getObjectIndex(i)
            if self.__objects[index].visible == True:
				objects.append(i)
        return objects
		    	    
    def getBehindNames(self, name):
        objects = []
        for i in self.__objects:
            if (i.location == name) and (i.lookBehind == True):
                objects.append(i.name)
        return objects                     
     
     
    def setUnderObjectsVisible(self, name, status):
        objects = self.getUnderNames(name)
        for i in objects:
            index = self.getObjectIndex(i)
            self.__objects[index].visible = status
            
    def getUnderObjectsVisible(self, name):
        objects = []
        for i in self.getUnderNames(name):       
            index = self.getObjectIndex(i)
            if self.__objects[index].visible == True:
				objects.append(i)
        return objects
		    	    
    def getUnderNames(self, name):
        objects = []
        for i in self.__objects:
            if (i.location == name) and (i.lookUnder == True):
                objects.append(i.name)
        return objects    
     
    def setAboveObjectsVisible(self, name, status):
        objects = self.getAboveNames(name)
        for i in objects:
            index = self.getObjectIndex(i)
            self.__objects[index].visible = status
            
    def getAboveObjectsVisible(self, name):
        objects = []
        for i in self.getAboveNames(name):       
            index = self.getObjectIndex(i)
            if self.__objects[index].visible == True:
				objects.append(i)
        return objects
		    	    
    def getAboveNames(self, name):
        objects = []
        for i in self.__objects:
            if (i.location == name) and (i.lookAbove == True):
                objects.append(i.name)
        return objects    
          
	
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
		
    def getEindex(self, name):
        index = 0
        for i in self.__exits:
            if i.name == name:
                return index
            index += 1
        return -1
        
    def getExitIndex(self, name):
        dlist = ['west','north','south','east']
        elist = self.getExitNames();
        if name in elist:
            return self.getEindex(name)
        else:
            for i in self.getRoomExits():
                index = self.getEindex(i) 
                if name in dlist:
                    if (self.__exits[index].direction == name):
                        return index
                else:
                    if (self.__exits[index].shortDescription == name):
                        return index
            return -1	
        
    def getGhostIndex(self,name):
		index = 0
		for i in self.__ghosts:
			if i.name == name:
				return index
			index += 1
		return -1



