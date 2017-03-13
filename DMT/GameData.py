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
#  CHANGES :  Code clean up and documentation.  
# 
#  VERSION     DATE      WHO        DETAIL
#    0.1    01/27/2017   JH    Initial Beta Version
#    0.2    02/02/2017   JH    
#    0.3    02/04/2017   JH    loadSavedGame, saveGame
#    0.4    02/13/2017   JH    Standardized method calls
#    1.0    02/26/2017   JH    First Production version
#    1.1    03/09/2017   JH    
########################################################
import json
import os
import re

PRIMITIVE_FILENAME = 'data/primitives.json'
DEPENDENCY_FILENAME = 'data/dependency.json'
SAVED_GAME_DIRECTORY = 'savedgames/'
MAXIMUM_HEALTH = 100

#Used to load class instance using a dedicated json file
class Filename():
    def __init__(self, f):
        filename = 'data/' + f
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
        self.__help = []
        self.__overhead = []
	
	#--------------------- Load New Game -----------------------
    def loadNewGame(self):
        """Loads a new game with predefined initial starting conditions"""
        self.__loadHelper(PRIMITIVE_FILENAME, True)
        
    #-------------------- Load Saved Game -----------------------
    def loadSavedGame(self, name=None, status=None):
        """Loads a saved game from the /savedgames directory"""
        
        #If 'loadgame' was called during game play, ensure this is what the player really wants.
        if status == False:
            response = raw_input("Quit current game and load a saved game (y/n)?: ")
            if response == "y":
                pass
            else:
                return ""
        
        filenames = os.listdir(SAVED_GAME_DIRECTORY)
        print "Saved games:"
        
        #List all files expect hidden files.
        for i in filenames:
            if not i.startswith('.'):
                print "   " + i
                
        response = raw_input("Please enter a filename: ")
        filename = SAVED_GAME_DIRECTORY + response
        
        if os.path.isfile(filename):
            if status == False:    #If overidding a game currently loaded ... clear list.
                self.__clearDynamicLists()
            self.__loadHelper(filename, status)
            return response + " loaded"
        else:
            print("File not found!")
            return 
            
    #----------------------- Clear Lists ------------------------- 
    def __clearDynamicLists(self):
        """Internal method used to clear lists that hold state dependent data"""
        del self.__players[:]
        del self.__bags[:]
        del self.__rooms[:]
        del self.__exits[:]
        del self.__objects[:]
        del self.__ghosts[:]
            
    #----------------------- Load Helper -------------------------    
    def __loadHelper(self, filename, status=None):
        """Internal method used to load JSON into class instances"""
            
        self.__primitives = json.loads(open(filename).read())
           
        for i in self.__primitives['players']:
            self.__players.append(Data(i))		
		
        for i in self.__primitives['bags']:
            self.__bags.append(Data(i))		
		
        for i in self.__primitives['rooms']:
            if status == True:
                self.__rooms.append(Filename(i['filename']))
            else:
                self.__rooms.append(Data(i))

        for i in self.__primitives['exits']:
            self.__exits.append(Data(i))
        
        for i in self.__primitives['objects']:
            self.__objects.append(Data(i))
        
        for i in self.__primitives['ghosts']:
			self.__ghosts.append(Data(i))
            
        if status != False:
            for i in self.__primitives['verbs']:
                self.__verbs.append(Data(i))
            
            for i in self.__primitives['prepositions']:
                self.__prepositions.append(Data(i))
        
            for i in self.__primitives['help']:
                self.__help.append(Data(i))
            
            for i in self.__primitives['overhead']:
                self.__overhead.append(Data(i))
            
            #Load the JSON file used to describe command dependencies and actions    
            self.__dependencies = json.loads(open(DEPENDENCY_FILENAME).read())


    #----------------------- Save Game -----------------------
    def saveGame(self, name=None, status=None):
        """Saves the current state of all instances to a JSON file"""
        s = {}
        s["players"] = []
        s["bags"] = []
        s["rooms"] = []
        s["exits"] = []
        s["objects"] = []
        s["ghosts"] = []
        s["verbs"] = []
        s["prepositions"] = []
        s["help"] = []
        s["overhead"] = []

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
        for i in self.__prepositions:
	        s["prepositions"].append(json.loads(json.dumps(i.__dict__)))
        for i in self.__help:
	        s["help"].append(json.loads(json.dumps(i.__dict__)))
        for i in self.__overhead:
	        s["overhead"].append(json.loads(json.dumps(i.__dict__)))

        response = raw_input("Please enter a filename: ")
        filename = SAVED_GAME_DIRECTORY + response
        
        if re.match(r'^[\A-Za-z][A-Za-z0-9]+$', response):
            with open(filename,'w') as outfile:
	            json.dump(s, outfile, indent=4)		
            return "Saved " + response
        else:
            return "Use only alphanumeric characters ... first character alpha"
            
    #-------------------- Dependencies---------------------------
    def getDependencies(self):
        """Returns JSON object containing command dependencies and actions"""
        return self.__dependencies
  

    #############################################################
	#                      Player Methods 
    #############################################################	
    
    #-----------------------------
    def isHealthMaximum(self, name=None, status=None):
        """Returns true if the player's health is at a maximum"""
        if self.__players[0].health == MAXIMUM_HEALTH:
            return True
        else:
            return False
            
    #-----------------------------   
    def restoreMaximumHealth(self, name=None, status=None):
        """Returns true if the player's health is at the maximum"""
        self.__players[0].health = MAXIMUM_HEALTH
        return "Player's health is at it's maximum level"
        
    #-----------------------------
    def getPlayerHealth(self):
        """Returns the players health level"""
        return self.__players[0].health
    
    #-----------------------------
    def setPlayerHealth(self, health):
        """Sets players health level"""
        self.__players[0].health = health
	    
    #-----------------------------    
    def adjustPlayerHealth(self, name, status=None):
        """Adjusts the players health based upon the healthpoints of an object"""
        index = self.getObjectIndex(name)
        if self.__players[0].health >= MAXIMUM_HEALTH and self.__objects[index].healthPoints >= 0:
            return "You are already at your maximum health level!"
        self.__players[0].health += self.__objects[index].healthPoints
        if self.__players[0].health >= MAXIMUM_HEALTH:
            self.__players[0].health = MAXIMUM_HEALTH
            return "You have maximized your health points!"
        if self.__players[0].health <= 0:
            self.__players[0].health = 0
            return "You are now deceased :("
        if self.__objects[index].healthPoints > 0:
            return "You have increased your health by " + str(self.__objects[index].healthPoints) + " points!"
        if self.__objects[index].healthPoints < 0:
            return "You have decreased your health by " + str(self.__objects[index].healthPoints) + " points!"
        if self.__objects[index].healthPoints == 0:
            return "No change to your health points!"

    #-----------------------------
    def getPlayerLocation(self):
        """Returns the room index the player is currently in"""
        return self.__players[0].location
    
    #-----------------------------
    def setPlayerLocation(self, location):
        """Sets the room index that the player is in"""
        self.__players[0].location = location
		
    #-----------------------------
    def isPlayerVisible(self):
        """Returns a Boolean indicating if the player is visible to ghosts"""
        return self.__players[0].visible
    
    #-----------------------------
    def setPlayerVisible(self, name=None, visible=True):
        """Boolean method that defines whether the player is visible or not"""
        self.__players[0].visible = visible   
        
    #-----------------------------
    def getPlayerProtectionPoints(self):
        """Returns the amount of protection currently worn by the player"""
        return self.__players[0].protection     
      
    #-----------------------------
    def setPlayerProtectionPoints(self, name, status):
        """Adjusts the players protection level"""
        index = self.getObjectIndex(name)
        if status:  # Add the object's protection points when equipped
            self.__players[0].protection += self.__objects[index].protectionPoints
        else:       # Subtract the object's protection points when unequipped
            self.__players[0].protection -= self.__objects[index].protectionPoints
	
	#-----------------------------	
    def movePlayer(self, direction, status=None):
        """Used to move a player from one room to another"""
        #Get exit's array index
        index = self.getExitIndex(direction) 
        #Set player's location to room the exit goes to. 
        self.__players[0].location = self.__exits[index].toRoom	
        #Get the new room's array index
        index = self.getRoomIndex(self.__players[0].location)
        return "You entered the " + self.__rooms[index].shortDescription
    
    #-----------------------------
    def getCurrentRoom(self):
        """Returns the short description of the room the player is in"""
        index = self.getRoomIndex(self.__players[0].location)
        return self.__rooms[index].shortDescription
	
    
    
    #############################################################
	#                   Inventory Methods 
    #############################################################	
    
    #-----------------------------
    def getInventoryCapacity(self):
        """Returns the amount of weight that can be held in inventory"""
        return self.__bags[0].capacity
        
    #-----------------------------
    def setInventoryCapacity(self, capacity):
        """Sets the amount of weight that can be held in inventory"""
        self.__bags[0].capacity = capacity
	
    #-----------------------------
    def getInventoryWeight(self):
        """Returns the total weight of all objects in inventory"""
        weight = 0
        for i in self.__bags[0].objects:
            index = self.getObjectIndex(i)
            if index >= 0:
                weight += self.__objects[index].weight
        return weight
        
	#-----------------------------
    def getInventoryObjects(self):
        """Returns a list of all objects in inventory"""
        return self.__bags[0].objects
        
    #-----------------------------    
    def getInventory(self, name=None, status=None):
        """Returns a formatted string of all objects in inventory"""
        inventory = ""
        if self.__bags[0].objects:
            inventory = "  Inventory Items" + "\n"
            for i in self.__bags[0].objects:
                inventory += "     Item: " + i + "\n"
        else:
            inventory = "No items are in the player's inventory"
        return inventory

    #-----------------------------
    def clearInventoryObjects(self):
        """Use to clear out all objects in inventory"""
        self.__bags[0].objects = []

    #-----------------------------
    def isSpaceInInventory(self, name):
        """Returns a Boolean indicating if there is enough room left
           in inventory to add the object (name)"""
        index = self.getObjectIndex(name)
        if ((self.getInventoryCapacity() - self.getInventoryWeight() 
		   - self.__objects[index].weight) > 0):
            return True
        else:
            return False

    #-----------------------------
    def addInventoryObject(self, name, status=None):
        """Adds an object to the player's inventory"""
        self.__bags[0].objects.append(name)
        index = self.getObjectIndex(name)
        #Set object's location to inventory	
        self.__objects[index].location = "inventory" 
	
    #-----------------------------	
    def removeInventoryObject(self, name, status=None):
        """Removes an object from the player's inventory"""
        self.__bags[0].objects.remove(name) 
    
     
     
     
     
    #############################################################
	#                     Room Methods 
    #############################################################  
    
    #-----------------------------
    def getRoomNames(self):
        """Returns a list of all room mnemonics used in the game"""
        rooms = []
        for i in self.__rooms:
            rooms.append(i.name)
        return rooms   
		
    #-----------------------------    
    def getRoomLongDescription(self, name=None, status=None):
        """Returns the long description of a room"""
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        return self.__rooms[index].longDescription
		
    #-----------------------------
    def getRoomShortDescription(self, name=None, status=None):
        """Returns the short description of a room"""
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        return self.__rooms[index].shortDescription
		
    #-----------------------------    
    def isRoomDiscovered(self):
        """Returns Boolean indicating if the room the player is in 
           has been visited before"""
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        return self.__rooms[index].discovered
		
    #-----------------------------
    def setRoomDiscovered(self, status):
        """Sets the discovered status of the room the player is in"""
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        self.__rooms[index].discovered = status
	
    #-----------------------------    
    def isRoomLighted(self, obj=None):
        """Returns Boolean indicating of the room the player is in
           is lighted"""
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        objectlighted = False
        """Look for all objects that are lighted and if a lighted 
           object is in either the player's inventory or in the room,
            set objectLighted to True"""
        for i in self.__objects:
            if i.lighted:
                if (self.isObjectInInventory(i.name) or self.isObjectInRoom(i.name)):
                    objectlighted = True   
        """If either the room is naturally lit or if objectLighted 
           is True, then return True, otherwise return False"""
        return (self.__rooms[index].lighted or objectlighted)
	
    #----------------------------- 
    def setRoomLighted(self, obj=None, status=None):
        """Set the lighted status of the room the player is currently in"""
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        self.__rooms[index].lighted = status
	
    #----------------------------- 	
    def getRoomObjects(self):
        """Returns a list of all objects contained within the room 
           the player is currently in"""
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        return self.__rooms[index].objects
	
    #----------------------------- 
    def addRoomObject(self, name, status=None):
        """Adds an object to the room the player is currently in"""
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        self.__rooms[index].objects.append(name)
        oindex = self.getObjectIndex(name)
        # set object's location to the current room	
        self.__objects[oindex].location = location	
	
    #----------------------------- 	
    def removeRoomObject(self, name, status=None):
        """Removes am objects from the room the player is currently in"""
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        self.__rooms[index].objects.remove(name)
        
    #----------------------------- 
    def getRoomExits(self):
        """Returns a list of mnemonics describing exits associated with
           the room the player is currently in"""
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        return self.__rooms[index].exits
	
    #----------------------------- 
    def getRoomExitDescriptions(self):
        """"Returns a list of short descriptions for every exit in the
            room the player is currently in"""
        exits = []
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        for i in self.__rooms[index].exits:
            eindex = self.getExitIndex(i)
            exits.append(self.__exits[eindex].shortDescription)
        return exits
        
    #-----------------------------	
    def clearRoomObjects(self):
        """Clears out all objects that are associated with the room the
           is currently in"""
        location = self.getPlayerLocation()
        index = self.getRoomIndex(location)
        self.__rooms[index].objects = []
		
		
        
        
    #############################################################
	#                     Exit Methods 
    ############################################################# 
    
    #-----------------------------
    def getExitNames(self):
        """Returns a list of mnemonics for all exits used in the game"""
        exits = []
        for i in self.__exits:
			exits.append(i.name)
        return exits
	
    #-----------------------------
    def getExitLongDescription(self, name):
        """Returns the long description of an exit"""
        index = self.getEindex(name)
        return self.__exits[index].longDescription	

    #-----------------------------
    def getExitShortDescription(self, name):
        """Returns the short description of an exit"""
        index = self.getExitIndex(name)
        return self.__exits[index].shortDescription
	
    #-----------------------------
    def getExitDirection(self, name):
        """Returns the direction, e.g. west, east, south, or north, 
           that the exit goes"""
        index = self.getExitIndex(name)
        return self.__exits[index].direction
	
    #-----------------------------
    def getExitKeyObject(self, name):
        """Returns the name of the key required to unlock an exit"""
        index = self.getExitIndex(name)
        return self.__exits[index].keyObject
	
    #-----------------------------	
    def isExitVisible(self, name):
        """Returns Boolean indicating if an exit is visible"""
        index = self.getExitIndex(name)
        return self.__exits[index].visible
      
    #-----------------------------    
    def setExitVisible(self, name, status):
        """Sets the visible status of an exit"""
        index = self.getExitIndex(name)
        self.__exits[index].visible = status
	
    #-----------------------------	
    def isExitUnlocked(self, name):
        """Returns a Boolean indicating if exit is unlocked"""
        index = self.getExitIndex(name)
        return self.__exits[index].unlocked
    
    #-----------------------------    
    def isExitInRoom(self, name):
        """Returns a Boolean indicating if an exit is in the room
           the player is currently in"""
        index = self.getExitIndex(name)
        if self.__exits[index].name in self.getRoomExits():
            return True
        return False
    
    #-----------------------------    
    def isExitKeyInInventory(self, name):
        """Returns Boolean indicating if the key required to unlock
           an exit is in the player's inventory"""
        index = self.getExitIndex(name)
        if self.__exits[index].keyObject in self.__bags[0].objects:
            return True
        #If exit does not require a key, then return True.
        if self.__exits[index].keyObject == '':
            return True
        return False   
    
    #-----------------------------    
    def setExitUnlocked(self, name, status):
        """"Sets an exit unlock status"""
        index = self.getExitIndex(name)
        self.__exits[index].unlocked = status
    
    #-----------------------------    
    def getExitToRoom(self, name):
        """Returns the room the an exit goes to"""
        index = self.getExitIndex(name)
        return self.__exits[index].toRoom
	
    
    
    
    #############################################################
	#                    Objects Methods 
    ############################################################# 
    
    #-----------------------------   
    def changeLocation(self, name, status=None):
        """Changes the location of the player based upon an object
           attibute value."""
        index = self.getObjectIndex(name)
        self.__players[0].location = self.__objects[index].keyObject	
    
    #-----------------------------     
    def getEquippedWeapon(self):
        """Returns the name of the weapon equipped by the player"""
        #Look through all items that are equipped
        for i in self.getEquippedObjects():
            #If item is a weapon, then return its name. Note that only
            #one weapon can be equipped at a time.
            if self.isObjectWieldable(i): 
                return i
        return None
        
    #-----------------------------     
    def isWeaponEquipped(self, name=None, status=None):
        """Returns a Boolean indicating if the player has a weapon equipped"""
        #Look through all items that are equipped
        for i in self.getEquippedObjects():
            #If item is a weapon, then return its name. Note that only
            #one weapon can be equipped at a time.
            if self.isObjectWieldable(i): 
                return True
        return False
    
    #----------------------------- 
    def isLookOnPossible(self, name):
        """Returns a Boolean indicating if player can "look on" the object"""
        index = self.getObjectIndex(name)
        return self.__objects[index].lookOn
    
    #----------------------------- 
    def isLookInsidePossible(self, name):
        """Returns a Boolean indicating if player can "look inside" the object"""
        index = self.getObjectIndex(name)
        return self.__objects[index].lookInside
    
    #----------------------------- 
    def isLookAbovePossible(self, name):
        """Returns a Boolean indicating if player can "look above" the object"""
        index = self.getObjectIndex(name)
        return self.__objects[index].lookAbove
        
    #----------------------------- 
    def isLookUnderPossible(self, name):
        """Returns a Boolean indicating if player can "look under" the object"""
        index = self.getObjectIndex(name)
        return self.__objects[index].lookUnder
    
    #-----------------------------     
    def isLookBehindPossible(self, name):
        """Returns a Boolean indicating if player can "look behind" the object"""
        index = self.getObjectIndex(name)
        return self.__objects[index].lookBehind
    
    #-----------------------------     
    def isObjectAccessible(self, name):
        """Returns a Boolean indicating if an object is either in the 
           player's inventory or in the room"""
        return (self.isObjectInInventory(name) or self.isObjectInRoom(name))    
    
    #----------------------------- 		
    def isObjectAcquirable(self, name):
        """Returns a Boolean indicating if an object can be picked up 
           and placed in inventory"""
        index = self.getObjectIndex(name)
        return self.__objects[index].acquirable		
	
    #----------------------------- 
    def isObjectDrinkable(self, name):
        """Returns a Boolean indicating if an object can be dranked"""
        index = self.getObjectIndex(name)
        return self.__objects[index].drinkable
      
    #-----------------------------     
    def isObjectEdible(self, name):
        """Returns a Boolean indicating if an object can be dranked"""
        index = self.getObjectIndex(name)
        return self.__objects[index].edible
    
    #-----------------------------     
    def isObjectEquippable(self, name):
        """Returns a Boolean indicating if an object can be worn or 
           held in the player's hand"""
        index = self.getObjectIndex(name)
        #If object is a weapon, first check if another weapon is already equipped.
        if self.__objects[index].wieldable:
            for i in self.getInventoryObjects():
                idx = self.getObjectIndex(i)
                if self.__objects[idx].equipped == True and self.__objects[idx].wieldable == True:
                    return False   #Player already has a weapon equipped.
        return self.__objects[index].equippable
    
    #----------------------------- 
    def isObjectEquipped(self, name):
        """Returns a Boolean indicating if an object is currently equipped""" 
        index = self.getObjectIndex(name)
        return self.__objects[index].equipped	
	
    #----------------------------- 
    def isObjectInInventory(self, name):
        """Returns a Boolean indicating if an object is in the player's
           inventory""" 
        for i in self.getInventoryObjects():
            if i == name:
                return True
        return False	
	
    #----------------------------- 	
    def isObjectInRoom(self, name):
        """Returns a Boolean indicating if an object is in the room the
           player is in""" 
        for i in self.getRoomObjects():
            if i == name:
                return True
        return False	
	
    #----------------------------- 	
    def isObjectKeyInInventory(self, name):
        """Returns a Boolean indicating if the key required to unlock 
           an object is in the player's inventory""" 
        index = self.getObjectIndex(name)
        if self.__objects[index].keyObject in self.__bags[0].objects:
            return True
        if self.__objects[index].keyObject == '':
            return True
        return False
     
    #-----------------------------     
    def isObjectLayable(self, name):
        """Returns a Boolean indicating if the player can lay on the object"""
        index = self.getObjectIndex(name)
        return self.__objects[index].layable		
		
    #-----------------------------      
    def isObjectLightable(self, name):
        """Returns a Boolean indicating if the object can be lighted"""
        index = self.getObjectIndex(name)
        return self.__objects[index].lightable		
       
    #-----------------------------     
    def isObjectLighted(self, name):
        """Returns a Boolean indicating if the object can be lit"""
        index = self.getObjectIndex(name)
        return self.__objects[index].lighted     
	
    #----------------------------- 	
    def isObjectLockable(self, name):
        """Returns a Boolean indicating if the object can be locked"""
        index = self.getObjectIndex(name)
        return self.__objects[index].lockable	
     
    #-----------------------------     
    def isObjectOpenable(self, name):
        """Returns a Boolean indicating if the object can be opened"""
        index = self.getObjectIndex(name)
        return self.__objects[index].openable	  
    
    #-----------------------------     
    def isObjectPickable(self, name):
        """Returns a Boolean indicating if the object can be picked"""
        index = self.getObjectIndex(name)
        return self.__objects[index].pickable	
	
    #----------------------------- 
    def isObjectPullable(self, name):
        """Returns a Boolean indicating if the object can be pulled"""
        index = self.getObjectIndex(name)
        return self.__objects[index].pullable	
	
    #----------------------------- 	
    def isObjectPushable(self, name):
        """Returns a Boolean indicating if the object can be pushed"""
        index = self.getObjectIndex(name)
        return self.__objects[index].pushable			
    
    #-----------------------------     
    def isObjectRead(self, name):
        """Returns a Boolean indicating if the object has been read"""
        index = self.getObjectIndex(name)
        return self.__objects[index].read        
    
    #-----------------------------     		
    def isObjectReadable(self, name):
        """Returns a Boolean indicating if an object can be read"""
        index = self.getObjectIndex(name)
        return self.__objects[index].readable	

    #----------------------------- 
    def isObjectSitable(self, name):
        """Returns a Boolean indicating if player can sit on the object"""
        index = self.getObjectIndex(name)
        return self.__objects[index].sitable	
    
    #-----------------------------    
    def isObjectUnlocked(self, name):
        """Returns a Boolean indicating if an object is unlocked"""
        index = self.getObjectIndex(name)
        return self.__objects[index].unlocked        
     
    #-----------------------------     				
    def isObjectUseable(self, name):
        """Returns a Boolean indicating if an object is useable
           This method has been deprecated"""
        index = self.getObjectIndex(name)
        return self.__objects[index].useable

    #----------------------------- 
    def isObjectVisible(self, name):
        """Returns a Boolean indicating if an object is visible"""
        index = self.getObjectIndex(name)
        return self.__objects[index].visible
    
    #-----------------------------     
    def isObjectWieldable(self, name):
        """Returns a Boolean indicating if an object is a weapon"""
        index = self.getObjectIndex(name)
        return self.__objects[index].wieldable		
	
    #----------------------------- 		 
    def getObjectLongDescription(self, name, state=None):
        """Returns the long description of the object"""
        index = self.getObjectIndex(name)
        return self.__objects[index].longDescription
	
    #----------------------------- 
    def getObjectShortDescription(self, name, state=None):
        """Returns the short description of the object"""
        index = self.getObjectIndex(name)
        return self.__objects[index].shortDescription   
     
    #----------------------------- 
    def getObjectWeight(self, name):
        """Returns the weight of the object"""
        index = self.getObjectIndex(name)
        return self.__objects[index].weight
	
    #----------------------------- 	
    def getObjectHealthPoints(self, name):
        """Returns the health points associated with an object that
           can be used to modify the player's health"""
        index = self.getObjectIndex(name)
        return self.__objects[index].healthPoints	
	
    #----------------------------- 
    def getObjectDamagePoints(self, name):
        """Returns the damage points associated with an object that 
           can be used to modify a ghost's health"""
        index = self.getObjectIndex(name)
        return self.__objects[index].damagePoints	
	
    #----------------------------- 	
    def getObjectProtectionPoints(self, name):
        """Returns the protection points associated with an object that
           and be used to modify the player's protection level"""
        index = self.getObjectIndex(name)
        return self.__objects[index].protectionPoints	
	
    #----------------------------- 	
    def getObjectKeyObject(self, name):
        """Returns the name of the key associated with an object"""
        index = self.getObjectIndex(name)
        return self.__objects[index].keyObject		
	
    #----------------------------- 	
    def getObjectLocation(self, name):
        """Returns the location of the object"""
        index = self.getObjectIndex(name)
        return self.__objects[index].location

    #----------------------------- 
    def setObjectLocation(self, name, location):
        """Sets the location of an object"""
        index = self.getObjectIndex(name)
        self.__objects[index].location = location	

    #----------------------------- 
    def setObjectVisible(self, name, status):
        """Sets the visible attribute of an object"""
        index = self.getObjectIndex(name)
        self.__objects[index].visible = status			
	
    #----------------------------- 		
    def setObjectLighted(self, name, status):
        """Sets the lighted attribute of an object"""
        index = self.getObjectIndex(name)
        self.__objects[index].lighted = status		
	
    #----------------------------- 	
    def setObjectUnlocked(self, name, status):
        """Sets the unlocked attribute of an object"""
        index = self.getObjectIndex(name)
        self.__objects[index].unlocked = status	
	
    #----------------------------- 
    def setObjectEquipped(self, name, status):
        """Sets the equipped attribute of an object"""
        index = self.getObjectIndex(name)
        self.__objects[index].equipped = status
	
    #----------------------------- 
    def setObjectRead(self, name, status):
        """Sets the read attribute of an object"""
        index = self.getObjectIndex(name)
        self.__objects[index].read = status

    #----------------------------- 
    def setObjectKeyObject(self, name, value):
        """Sets the key associated with an object"""
        index = self.getObjectIndex(name)
        self.__objects[index].keyObject	= value
    
    #-----------------------------     
    def getVisibleObjects(self):
        """Returns a list of all visible objects in the room the 
           player is in"""
        objects = []
        room = self.getPlayerLocation()
        #Determine if room is lit.
        roomLit = self.isRoomLighted(room)
        #For all objects in room, determine if the object is visible
        for i in self.getRoomObjects():
            index = self.getObjectIndex(i)
            #If room is lit and object is visible, then add to list
            if (self.__objects[index].visible == True) and roomLit:
                objects.append(i)
        return objects

    #----------------------------- 
    def getObjectNames(self):
        """Returns a list of all object names used in the game"""
        objects = []
        for i in self.__objects:
			objects.append(i.name)
        return objects						
		
    #----------------------------- 	
    def setOnObjectsVisible(self, name, status):
        """Set the visible attribute of all items that are "on" object"""
        objectNames = self.__getLookObjectNames(name, "on")
        return self.__setObjectsVisible(objectNames, status)
    
    #-----------------------------         
    def getOnObjectsVisible(self, name):
        """Returns a list of all items that are visible "on" an object"""
        return self.__getLookObjectNames(name, "on")

    #-----------------------------  
    def setInsideObjectsVisible(self, name, status):
        """Set the visible attribute of all items that are "inside" object"""
        objectNames = self.__getLookObjectNames(name, "inside")
        return self.__setObjectsVisible(objectNames, status)
    
    #-----------------------------         
    def getInsideObjectsVisible(self, name):
        """Returns a list of all items that are visible "inside" an object"""
        return self.__getLookObjectNames(name, "inside")

    #-----------------------------  
    def setUnderObjectsVisible(self, name, status):
        """Set the visible attribute of all items that are "under" object"""
        objectNames = self.__getLookObjectNames(name, "under")
        return self.__setObjectsVisible(objectNames, status)
    
    #-----------------------------         
    def getUnderObjectsVisible(self, name):
        """Returns a list of all items that are visible "under" an object"""
        return self.__getLookObjectNames(name, "under")

    #-----------------------------  
    def setBehindObjectsVisible(self, name, status):
        """Set the visible attribute of all items that are "behind" object"""
        objectNames = self.__getLookObjectNames(name, "behind")
        return self.__setObjectsVisible(objectNames, status)
    
    #-----------------------------         
    def getBehindObjectsVisible(self, name):
        """Returns a list of all items that are visible "behind" an object"""
        return self.__getLookObjectNames(name, "behind")
    
    #-----------------------------  
    def setAboveObjectsVisible(self, name, status):
        """Set the visible attribute of all items that are "above" object"""
        objectNames = self.__getLookObjectNames(name, "above")
        return self.__setObjectsVisible(objectNames, status)
    
    #-----------------------------         
    def getAboveObjectsVisible(self, name):
        """Returns a list of all items that are visible "above" an object"""
        return self.__getLookObjectNames(name, "above")

    #-----------------------------  
    def __setObjectsVisible(self, objects, status):
        """Returns a list of objects that visible in 'objects'"""
        response = ""
        objs = []
        for i in objects:
            index = self.getObjectIndex(i)
            objs.append(i)
            self.__objects[index].visible = status
        if len(objs) > 0:
            count = 0
            response += "You see the following item(s): "
            for i in objs:
                count += 1
                if count == len(objs):
                    response += i
                else:
                    response += i + ", "
        else:
            response += "You do not see anything"
        return response      
          
    #----------------------------- 	    	    
    def __getLookObjectNames(self, name, look):
        """Returns a list of items that are spatially associated with object"""
        objects = []
        for i in self.__objects:
            if (i.location == name):
                if look == "above" and i.lookAbove == True:
                    objects.append(i.name)
                if look == "on" and i.lookOn == True:
                    objects.append(i.name)
                if look == "behind" and i.lookBehind == True:
                    objects.append(i.name)
                if look == "under" and i.lookUnder == True:
                    objects.append(i.name)
                if look == "inside" and i.lookInside == True:
                    objects.append(i.name)
        return objects    
  
    #----------------------------- 	
    """Adjust the damage of weapon objects"""
    def adjustWeaponPotential(self, name=None, status=None):
        for i in self.__objects:
            if (i.wieldable):
                if status:
                    i.damagePoints *= 2
                else:
                    i.damagePoints *= 0.5
                    
 
 
 
  
    #############################################################
	#                    Ghost Methods 
    #############################################################         
          
          
    #-----------------------------
    def getGhostNames(self):
        """Returns a list of names of ghost used in the game"""
        ghosts = []
        for i in self.__ghosts:
			ghosts.append(i.name)
        return ghosts	
    
    #-----------------------------    
    def getGhostLongDescription(self, name, status=None):
        """Returns the long description of a ghost"""
        index = self.getGhostIndex(name)
        return self.__ghosts[index].longDescription
	
    #----------------------------- 	
    def getGhostShortDescription(self, name, status=None):
        """Returns the short description of a ghost"""
        index = self.getGhostIndex(name)
        return self.__ghosts[index].shortDescription
	
    #----------------------------- 
    def isGhostVisible(self, name):
        """Returns a Boolean indicating if the ghost is visible"""
        index = self.getGhostIndex(name)
        return self.__ghosts[index].visible
	
    #-----------------------------	
    def setGhostVisible(self, name, status):
        """Sets the visible attribute of the ghost"""
        index = self.getGhostIndex(name)
        self.__ghosts[index].visible = status
	
    #----------------------------- 	
    def getGhostLocation(self, name, status=None):
        """Returns the room nmemonic the ghost is in"""
        index = self.getGhostIndex(name)
        return self.__ghosts[index].location

    #-----------------------------		
    def setGhostLocation(self, name, location):
        """Sets the room the ghost is in"""
        index = self.getGhostIndex(name)
        self.__ghosts[index].location = location
	
    #----------------------------- 	
    def getGhostHealth(self, name, status=None):
        """Returns the health level of the ghost"""
        index = self.getGhostIndex(name)
        return self.__ghosts[index].health
	
    #----------------------------- 	
    def setGhostHealth(self, name, health):
        """Sets the health level of the ghost"""
        index = self.getGhostIndex(name)
        self.__ghosts[index].health = health
        
    #----------------------------- 
    def getGhostDamagePoints(self, name, status=None):
        """Returns the damage points the ghost can inflect on the player"""
        index = self.getGhostIndex(name)
        return self.__ghosts[index].damagePoints
        
    #----------------------------- 
    def attackGhost(self, name, status=None):
        return
				
	    
    #############################################################
	#                    Index Methods 
    #############################################################   
        
    #-----------------------------   
    def getObjectIndex(self, name):
        """Returns the array index that the object instance is stored in"""
        index = 0
        for i in self.__objects:
            if i.name == name:
                return index
            index += 1
        return -1    #Return -1 if index not found
	
    #----------------------------- 
    def getRoomIndex(self, name):
        """Returns the array index that the room instance is stored in"""
        index = 0
        for i in self.__rooms:
            if i.name == name:
                return index
            index += 1
        return -1    #Return -1 if index not found
	
    #----------------------------- 	
    def getEindex(self, name):
        """Returns the array index that the exit instance is stored in"""
        index = 0
        for i in self.__exits:
            if i.name == name:
                return index
            index += 1
        return -1   #Return -1 if index not found
       
    #-----------------------------     
    def getExitIndex(self, name):
        """Used to return an exit's array index corresponding to name.
           Name can be given in one of three forms.
               i. A direction such as west, north, east, or south.
              ii. An internal mnemonic used to identify exits.
             iii. A short description of the exit
            """
        #Create list of directions
        dlist = ['west','north','south','east'] 
        
        #Get list of all exit mnemonics used in the game
        elist = self.getExitNames(); 
        
        #If name is a mnemonic, return it's array index value
        if name in elist:  
            return self.getEindex(name)
        else:
            """Name is either a direction or a short description of an
               exit in the room the player is in."""
            for i in self.getRoomExits():
                index = self.getEindex(i) 
                """If name is a direction and an exit exist in the room 
                   going in that direction, then return index""" 
                if name in dlist: 
                    if (self.__exits[index].direction == name):
                        return index
                else:
                    """If exit with short description exits in room,
                       then return index"""
                    if (self.__exits[index].commandName == name):
                        return index
                        
            return -1	#Return -1 if index not found
      
      
    #-----------------------------     
    def getGhostIndex(self,name):
        """Returns the array index that the ghost instance is stored in"""
        index = 0
        for i in self.__ghosts:
            if i.name == name:
                return index
            index += 1
        return -1   #Return -1 if index not found

    #############################################################
	#               Miscellaneous Methods 
    #############################################################


    #----------------------------- 
    def getHelp(self, name=None, status=None):
        """Returns formatted string describing all verbs used in game"""
        help = "Verbs used in Haunted Dungeon\n"
        for i in self.__help:
            help += i.verb + "\n"
            help += i.description + "\n"
        return help
        
    #----------------------------- 
    def getGhosts(self, name, status=None):
        """Returns formatted string describing status of all ghosts used in game"""
        ghosts = ""
        if name == "all":
            for i in self.__ghosts:
                loc_mnemonic = self.getGhostLocation(i.name)
                index = self.getRoomIndex(loc_mnemonic)
                location = self.__rooms[index].shortDescription
                name = '%14s' % (i.shortDescription + "   ")
                health = '%-12s' % ("Health:" + str(i.health))
                damage = '%-12s' % ("Damage:" + str(i.damagePoints))
                location = '%-25s' % ("Location:" + location)
                ghosts += name + health + damage + location + "\n"
        else:
                ghost_index = self.getGhostIndex(name)
                i = self.__ghosts[ghost_index]
                loc_mnemonic = self.getGhostLocation(i.name)
                index = self.getRoomIndex(loc_mnemonic)
                location = self.__rooms[index].shortDescription
                ghosts += i.shortDescription + "  Health:" + str(i.health) +  "  Damage:" + str(i.damagePoints) + "   Location:"  + location + "\n"
                          
        return ghosts


    #----------------------------- 
    def getVerbs(self, name=None, status=None):
        """Returns a list of all verbs supported in the game"""
        verbs = []
        for i in self.__verbs:
            verbs.append(i.verb)
        return verbs
      
    #-----------------------------     
    def getVerbDescriptions(self, name=None, status=None):
        """Returns a list of verb descriptions"""
        descriptions = []
        for i in self.__verbs:
            descriptions.append(i.description)
        return descriptions
    
    #----------------------------- 
    def getPrepositions(self, name=None, status=None):
        """Returns a list of prepositions used in the game"""
        prepositions = []
        for i in self.__prepositions:
            prepositions.append(i.preposition)
        return prepositions
       
    #-----------------------------     
    def getObjects(self, name=None, status=None):
        """Returns a list of objects used in the game"""
        objects = []
        for i in self.__objects:
			objects.append(i.name)
        return objects	
     
    #----------------------------- 
    def getExits(self, name=None, status=None):
        """Returns a list of all exit names used in the game"""
        exits = []
        for i in self.__exits:
			exits.append(i.commandName)
        for i in self.__overhead:
            exits.append(i.word)
        return exits	
    
    #-----------------------------     
    def getVerbPrepositionCombos(self):
        """Returns a JSON object of all verb-prepositions combinations"""
        combo = {}
        for i in self.__verbs:
            combo[i.verb] = i.prepositions
        return combo

    #----------------------------- 
    def getEquippedObjects(self):
        """Returns a list of all objects that are equipped"""
        objects = []
        for i in self.getInventoryObjects():
            index = self.getObjectIndex(i)
            if self.__objects[index].equipped:
                objects.append(i)
        return objects
    
    #----------------------------- 
    def getCommandTuples(self):
        """Returns a list of all commands supported in the game"""
        commands = []
        for i in self.__dependencies['commands']:
            commands.append(i['tuple'])
        return commands

    #----------------------------- 
    def isCommandTuple(self, command):
        """Returns a Boolean indicating if a command is supported"""
        for i in self.__dependencies['commands']:
            if command == i['tuple']:
                return True
        return False
   
            
    
