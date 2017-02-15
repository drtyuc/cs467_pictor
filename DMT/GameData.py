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
#      This file has been tested for basic functionally
#      using attribute accuracy using testDataMethods.py     
#      and testDataAttributes.py
# 
#
#  AUTHOR : Jerry Hayes        START DATE : 01/27/2017
#
#  CHANGES :  Added loadSavedGame and saveGame methods.  
# 
#  VERSION     DATE      WHO        DETAIL
#    0.1    01/27/2017   JH    Initial Beta Version
#    0.2    02/02/2017   JH    
#    0.3    02/04/2017   JH    loadSavedGame, saveGame
#    0.4    02/06/2017   JH    Standardized method calls
########################################################
import json
import os.path

PRIMITIVE_FILENAME = 'data/primitives.json'
DEPENDENCY_FILENAME = 'data/dependency.json'
SAVED_GAME_DIRECTORY = 'savedgames/'

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
        self.__verbs = []
        self.__prepositions = []
        self.__dependencies = []
	
	#--------------------- Load New Game -----------------------
    def loadNewGame(self):
        self.loadHelper(PRIMITIVE_FILENAME)
        
    #-------------------- Load Saved Game -----------------------
    def loadSavedGame(self):
        response = raw_input("Please enter a filename: ")
        filename = SAVED_GAME_DIRECTORY + response
        
        if os.path.isfile(filename):
            self.loadHelper(filename)
        else:
            print("File not found!")
        
    #----------------------- Load Helper -------------------------    
    def loadHelper(self, filename):
            
        self.__primitives = json.loads(open(filename).read())
           
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
            
        for i in self.__primitives['verbs']:
            self.__verbs.append(Data(i))
            
        for i in self.__primitives['prepositions']:
            self.__prepositions.append(Data(i))
            
        self.__dependencies = json.loads(open(DEPENDENCY_FILENAME).read())

    #----------------------- Save Game -----------------------
    def saveGame(self):
        s = {}
        s["players"] = []
        s["bags"] = []
        s["rooms"] = []
        s["exits"] = []
        s["objects"] = []
        s["ghosts"] = []
        s["verbs"] = []
        s["prepositions"] = []

        for i in self.__players:
	        s["players"].append(json.loads(json.dumps(i.__dict__)))
        for i in self.__bags:
	        s["bags"].append(json.loads(json.dumps(i.__dict__)))
        for i in self.__rooms:
	        s["rooms"].append(json.loads(json.dumps(i.__dict__)))
        for i in self.__exits:
	        s["exits"].append(json.loads(json.dumps(i.__dict__)))
        for i in self.__objects:
	        s["objects"].append(json.loads(json.dumps(i.__dict__)))
        for i in self.__ghosts:
	        s["ghosts"].append(json.loads(json.dumps(i.__dict__)))
        for i in self.__verbs:
	        s["verbs"].append(json.loads(json.dumps(i.__dict__)))
        for i in self.__prepostions:
	        s["prepositions"].append(json.loads(json.dumps(i.__dict__)))

        response = raw_input("Please enter a filename: ")
        filename = SAVED_GAME_DIRECTORY + response

        with open(filename,'w') as outfile:
	        json.dump(s, outfile, indent=4)		
            
    #-------------------- Dependencies---------------------------
    def getDependencies(self):
        return self.__dependencies

	
	#------------------ Player Methods ---------------------------		
    def getPlayerHealth(self):
		return self.__players[0].health
		
    def getPlayerLocation(self):
        return self.__players[0].location
	    
    def isPlayerVisible(self):
	    return self.__players[0].visible
        
    def setPlayerHealth(self, health):
        self.__players[0].health = health
	    
    def adjustPlayerHealth(self, name, status=None):
		index = self.getObjectIndex(name)
		self.__players[0].health += self.__objects[index].healthPoints
	
    def setPlayerLocation(self, location):
		self.__players[0].location = location
		
    def setPlayerVisible(self, visible):
		self.__players[0].visible = visible
		
    def movePlayer(self, direction, status=None):
        index = self.getExitIndex(direction)
        self.__players[0].location = self.__exits[index].toRoom	
    
    def getCurrentRoom(self):
        index = self.getRoomIndex(self.__players[0].location)
        return self.__rooms[index].shortDescription
	
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

    def addInventoryObject(self, name, status=None):
        self.__bags[0].objects.append(name)
        index = self.getObjectIndex(name)
        self.__objects[index].location = "inventory"	
		
    def removeInventoryObject(self, name, status=None):
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
	
    def isRoomLighted(self, obj=None):
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        objectlighted = False
        for i in self.__objects:
            if i.lighted:
                if (self.isObjectInInventory(i.name) or self.isObjectInRoom(i.name)):
                    objectlighted = True   
        return (self.__rooms[index].lighted or objectlighted)
	
    def setRoomLighted(self, obj, status):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		self.__rooms[index].lighted = status
		
    def getRoomObjects(self):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		return self.__rooms[index].objects
	
    def addRoomObject(self, name, status=None):
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        self.__rooms[index].objects.append(name)
        oindex = self.getObjectIndex(name)
        self.__objects[oindex].location = location		
		
    def removeRoomObject(self, name, status=None):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		self.__rooms[index].objects.remove(name)
        
    def getRoomExits(self):
		location = self.getPlayerLocation()
		index = self.getRoomIndex(location)
		return self.__rooms[index].exits
	
    def getRoomExitDescriptions(self):
        exits = []
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        for i in self.__rooms[index].exits:
            eindex = self.getExitIndex(i)
            exits.append(self.__exits[eindex].shortDescription)
        return exits
		
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
    def changeLocation(self, name, status=None):
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
        return (self.isObjectInInventory(name) or self.isObjectInRoom(name))    
    		
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
        if self.__objects[index].wieldable:
            for i in self.getInventoryObjects():
                idx = self.getObjectIndex(i)
                if self.__objects[index].equipped == True:
                    return False
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
			 
    def getObjectLongDescription(self, name, state=None):
		index = self.getObjectIndex(name)
		return self.__objects[index].longDescription
	
    def getObjectShortDescription(self, name, state=None):
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

    def setObjectKeyObject(self, name, value):
		index = self.getObjectIndex(name)
		self.__objects[index].keyObject	= value
        
    def getVisibleObjects(self):
        objects = []
        room = self.getPlayerLocation()
        roomLit = self.isRoomLighted(room)
        for i in self.getRoomObjects():
            index = self.getObjectIndex(i)
            if (self.__objects[index].visible == True) and roomLit:
                objects.append(i)
        return objects


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
    
    def adjustGhostHealth(self, name, status=None):
        x = 1
				
	    
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

#----------------- Miscellaneous Methods -------------------  

    def getVerbs(self):
        verbs = []
        for i in self.__verbs:
            verbs.append(i.verb)
        return verbs
        
    def getVerbDescriptions(self):
        descriptions = []
        for i in self.__verbs:
            descriptions.append(i.description)
        return descriptions
    
    def getPrepositions(self):
        prepositions = []
        for i in self.__prepositions:
            prepositions.append(i.preposition)
        return prepositions
        
    def getObjects(self):
        objects = []
        for i in self.__objects:
			objects.append(i.name)
        return objects	
        
    def getExits(self):
        exits = ['west','north','south','east']
        for i in self.__exits:
			exits.append(i.shortDescription)
        return exits	
        
    def getVerbPrepositionCombos(self):
        combo = {}
        for i in self.__verbs:
            combo[i.verb] = i.prepositions
        return combo

    def getEquippedObjects(self):
        objects = []
        for i in self.getInventoryObjects():
            index = self.getObjectIndex(i)
            if self.__objects[index].equipped:
                objects.append(i)
        return objects
    
    def getCommandTuples(self):
        commands = []
        for i in self.__dependencies['commands']:
            commands.append(i['tuple'])
        return commands

    def isCommandTuple(self, command):
        for i in self.__dependencies['commands']:
            if command == i['tuple']:
                return True
        return False
   
            
    
