from DMT.GameData import DataManager
import unittest

dm = DataManager()
dm.loadNewGame()

class Player(unittest.TestCase):
    #P1  
    def test_adjustPlayerHealth(self):
        dm.setPlayerHealth(50)
        dm.adjustPlayerHealth('green apple')
        self.assertEqual(dm.getPlayerHealth(), 65, "#P1: FAILED adjustPlayerHealth")
    #P2
    def test_isPlayerVisible(self):
        dm.setPlayerVisible("", True)
        self.assertTrue(dm.isPlayerVisible(), "#P2  FAILED isPlayerVisible")
    #P3
    def test_setPlayerVisible(self):
        dm.setPlayerVisible("", False)
        self.assertFalse(dm.isPlayerVisible(), "#P3  FAILED setPlayerVisible")
    #P4
    def test_getPlayerLocation(self):
        dm.setPlayerLocation("ce")
        self.assertEqual(dm.getPlayerLocation(), "ce",  "#P4  FAILED getPlayerLocation")
    #P5
    def test_setPlayerLocation(self):
        dm.setPlayerLocation("kt")
        self.assertEqual(dm.getPlayerLocation(), "kt",  "#P5  FAILED setPlayerLocation")
    #P6
    def test_movePlayer1(self):
        dm.setPlayerLocation('ce')
        dm.movePlayer('south')
        self.assertEqual(dm.getPlayerLocation(), 'ot', "#P6  FAILED movePlayer1")
    #P7
    def test_movePlayer2(self):
        dm.setPlayerLocation('ce')
        dm.movePlayer('long dark tunnel')
        self.assertEqual(dm.getPlayerLocation(), 'pw', "#P7  FAILED movePlayer2")


class Inventory(unittest.TestCase):       
    #I1    
    def test_InventoryCapacity(self):
        dm.setInventoryCapacity(150)
        self.assertEqual(dm.getInventoryCapacity(), 150,  "1#I1  FAILED InventoryCapacity")
    #I2
    def test_addInventoryObject(self):
        olist = ['armor', 'machete', 'bottle of water']
        dm.clearInventoryObjects()
        dm.addInventoryObject("armor")
        dm.addInventoryObject("machete")
        dm.addInventoryObject("bottle of water")
        self.assertItemsEqual(dm.getInventoryObjects(), olist,  "#I2  FAILED addInventoryObject")
        self.assertEqual(dm.getObjectLocation('bottle of water'), 'inventory', "#I2   FAILED addInventoryObject")
    #I3
    def test_removeInventoryObject(self):
        olist = ['armor', 'bottle of water']
        dm.clearInventoryObjects()
        dm.addInventoryObject("armor")
        dm.addInventoryObject("machete")
        dm.addInventoryObject("bottle of water")
        dm.removeInventoryObject("machete")
        self.assertItemsEqual(dm.getInventoryObjects(), olist,  "#I3  FAILED removeInventoryObject")
      
    #I4
    def test_getInventoryWeight(self):
        dm.clearInventoryObjects()       
        dm.addInventoryObject("armor")
        dm.addInventoryObject("green apple")
        self.assertEqual(dm.getInventoryWeight(),  85, "#I4  FAILED getInventoryWeight")
    #I5
    def test_isSpaceInInventory1(self):
        dm.clearInventoryObjects()
        dm.addInventoryObject("armor")
        self.assertTrue(dm.isSpaceInInventory("green apple"), "#I5  FAILED  isSpaceInInventory")
    #I6
    def test_isSpaceInInventory2(self):
        dm.clearInventoryObjects() 
        dm.addInventoryObject("armor")
        self.assertFalse(dm.isSpaceInInventory("safe"), "#I6  FAILED  isSpaceInInventory")
 
 
class Rooms(unittest.TestCase):  
    #R1
    def test_getRoomNames(self):
        rlist = ['ap', 'ar', 'bd', 'bh', 'ca', 'ce', 'cl', 'ct', 'hw', 'jl', 'kt', 'ot',
                 'pw', 'sq', 'sr', 'tr', 'wl']
        self.assertItemsEqual(dm.getRoomNames(), rlist,  "#R1  FAILED  getRoomNames")
    #R2
    def test_getRoomLongDescription(self):
        dm.setPlayerLocation('kt')
        self.assertEqual(dm.getRoomLongDescription(), "A room used to perpare meals for the dungeon's inhabitants.  It has skylighting in the ceiling which highlights the filthy conditions of the room.", "#R2  Failed getRoomLongDescription")
    #R3
    def test_getRoomShortDescription(self):
        dm.setPlayerLocation('kt')
        self.assertEqual(dm.getRoomShortDescription(), "Kitchen", "#R3  Failed getRoomShortDescription")
    #R4
    def test_isRoomDiscovered(self):
        dm.setPlayerLocation('kt')
        dm.setRoomDiscovered(True)
        self.assertTrue(dm.isRoomDiscovered(), "#R4  Failed  isRoomDiscovered")
    #R5
    def test_setRoomDiscovered(self):
        dm.setPlayerLocation('kt')
        dm.setRoomDiscovered(False)
        self.assertFalse(dm.isRoomDiscovered(), "#R5  Failed  setRoomDiscovered")
   
    #R6
    def test_isRoomLighted(self):
        dm.setPlayerLocation('kt')
        self.assertTrue(dm.isRoomLighted(), "#R6  Failed  isRoomLighted")
        dm.setPlayerLocation('bd')
        self.assertFalse(dm.isRoomLighted(), "#R6  Failed  isRoomLighted")
        dm.addInventoryObject('brass lantern')
        self.assertFalse(dm.isRoomLighted(), "#R6  Failed  isRoomLighted")
        dm.setObjectLighted('brass lantern', True)
        self.assertTrue(dm.isObjectLighted('brass lantern'), "#R6  Failed  isRoomLighted")
        self.assertTrue(dm.isRoomLighted(), "#R6  Failed  isRoomLighted")
        dm.removeInventoryObject('brass lantern')
        dm.addRoomObject('brass lantern')
        self.assertTrue(dm.isRoomLighted(), "#R6  Failed  isRoomLighted")
        dm.setPlayerLocation('jl')
        self.assertFalse(dm.isRoomLighted(), "#R6  Failed  isRoomLighted")
        dm.setPlayerLocation('bd')
        self.assertTrue(dm.isRoomLighted(), "#R6  Failed  isRoomLighted")
    #R7
    def test_setRoomLighted(self):
        dm.setPlayerLocation('kt')
        dm.setRoomLighted('kt', False)
        self.assertFalse(dm.isRoomLighted(), "#R7  Failed setRoomLighted")
    #R8
    def test_addRoomObject(self):
        olist = ['sign1', 'tree1','safe1']
        dm.setPlayerLocation('ot')
        dm.clearRoomObjects()
        dm.addRoomObject('sign1')
        dm.addRoomObject('tree1')
        dm.addRoomObject('safe1')
        self.assertItemsEqual(dm.getRoomObjects(), olist,  "#R8  FAILED  addRoomObject") 
        self.assertEqual(dm.getObjectLocation('safe1'), 'ot',  "#R8  FAILED  addRoomObject")   
    #R9
    def test_removeRoomObject(self):
        olist = ['sign1', 'tree1','safe1']
        dm.setPlayerLocation('ot')
        dm.clearRoomObjects()
        dm.addRoomObject('sign1')
        dm.addRoomObject('tree1')
        dm.addRoomObject('bones1')
        dm.addRoomObject('safe1')
        dm.removeRoomObject('bones1')
        self.assertItemsEqual(dm.getRoomObjects(), olist,  "#R9  FAILED  removeRoomObject")  


class Exits(unittest.TestCase):                     
    #E1
    def test_getExitNames(self):
        elist = ['ap1', 'ar1', 'ar2', 'ar3', 'bd1', 'bh1', 'bh2', 'ca1', 'ca2', 'ce1', 'ce2',
                 'cl1', 'hw1', 'hw2', 'hw3', 'jl1', 'jl2', 'kt1', 'kt2', 'kt3', 'out',
                 'pw1', 'pw2', 'sq1', 'sq2', 'sr1', 'tr1', 'wl1', 'wl2']
        self.assertItemsEqual(dm.getExitNames(), elist,  "#E1  FAILED  getExitNames") 
    #E2
    def test_getExitLongDescription(self):
        self.assertEqual(dm.getExitLongDescription('kt1'), "A pair of 'smoky glazed doors' on the west wall that leads to the Common Area", "#E2 Failed  getExitLongDesciption")
    #E3
    def test_getExitShortDescription(self):
        self.assertEqual(dm.getExitShortDescription('kt1'), "'Smoky glazed doors' on the west wall", "#E3 Failed  getExitShortDesciption")
    #E4
    def test_isExitVisible(self):
        dm.setExitVisible('kt1', False)
        self.assertFalse(dm.isExitVisible('kt1'),  "#E4 Failed  isExitVisible")
    #E5
    def test_setExitVisible(self):
        dm.setExitVisible('kt1', True)
        self.assertTrue(dm.isExitVisible('kt1'),  "#E5 Failed  setExitVisible")
        dm.setExitVisible('kt1', False)
        self.assertFalse(dm.isExitVisible('kt1'),  "#E5 Failed  setExitVisible")
        dm.setPlayerLocation('kt')
        dm.setExitVisible('west', True)
        self.assertTrue(dm.isExitVisible('west'),  "#E5 Failed  setExitVisible")
        dm.setExitVisible('west', False)
        self.assertFalse(dm.isExitVisible('west'),  "#E5 Failed  setExitVisible")
        dm.setExitVisible('Exit going west', True)
        self.assertTrue(dm.isExitVisible('Exit going west'),  "#E5 Failed  setExitVisible")
        dm.setExitVisible('Exit going west', False)
        self.assertFalse(dm.isExitVisible('Exit going west'),  "#E5 Failed  setExitVisible")

    #E6
    def test_isExitUnlocked(self):
        dm.setExitUnlocked('kt1', False)
        self.assertFalse(dm.isExitUnlocked('kt1'),  "#E6 Failed  isExitUnlocked")

    #E7
    def test_setExitUnlocked(self):
        dm.setExitUnlocked('kt1', True)
        self.assertTrue(dm.isExitUnlocked('kt1'),  "#E7 Failed  setExitUnlocked") 
        dm.setExitUnlocked('kt1', False)
        self.assertFalse(dm.isExitUnlocked('kt1'),  "#E7 Failed  setExitUnlocked") 
        dm.setPlayerLocation('kt')
        dm.setExitUnlocked('west', True)
        self.assertTrue(dm.isExitUnlocked('west'),  "#E7 Failed  setExitUnlocked") 
        dm.setExitUnlocked('west', False)
        self.assertFalse(dm.isExitUnlocked('west'),  "#E7 Failed  setExitUnlocked") 
        dm.setExitUnlocked('Exit going west', True)
        self.assertTrue(dm.isExitUnlocked('Exit going west'),  "#E7 Failed  setExitUnlocked") 
        dm.setExitUnlocked('Exit going west', False)
        self.assertFalse(dm.isExitUnlocked('Exit going west'),  "#E7 Failed  setExitUnlocked") 

    #E8
    def test_isExitInRoom(self):
        dm.setPlayerLocation('ce')
        self.assertTrue(dm.isExitInRoom('ce1'), "#E8  Failed isExitInRoom")
        self.assertTrue(dm.isExitInRoom('south'), "#E8  Failed isExitInRoom")
        self.assertTrue(dm.isExitInRoom('corrugated steel door'), "#E8  Failed isExitInRoom")
        self.assertFalse(dm.isExitInRoom('bh1'), "#E8  Failed isExitInRoom")
        self.assertFalse(dm.isExitInRoom('west'), "#E8  Failed isExitInRoom")
        self.assertFalse(dm.isExitInRoom('Exit going west'), "#E8  Failed isExitInRoom")
    #E9
    def test_isExitKeyInInventory(self):
        dm.clearInventoryObjects()
        self.assertFalse(dm.isExitKeyInInventory('ce1'), "#E9  Failed  isExitKeyInInventory")
        dm.addInventoryObject('golden key')
        self.assertTrue(dm.isExitKeyInInventory('ce1'), "#E9  Failed  isExitKeyInInventory")
        self.assertTrue(dm.isExitKeyInInventory('ce2'), "#E9  Failed  isExitKeyInInventory")        
        
        
    
class Objects(unittest.TestCase):
    #O1
    def test_isObjectInInventory(self):
        dm.clearInventoryObjects()
        dm.addInventoryObject('green apple')
        self.assertTrue(dm.isObjectInInventory('green apple'), "#O1 Failed  isObjectInInventory")
        self.assertFalse(dm.isObjectInInventory('armor'), "#O1 Failed  isObjectInInventory")
    #O2
    def test_isObjectInRoom(self):
        dm.setPlayerLocation('ap')
        dm.clearRoomObjects()
        dm.addRoomObject('green apple')
        self.assertTrue(dm.isObjectInRoom('green apple'), "#O2 Failed  isObjectInRoom")
        self.assertFalse(dm.isObjectInRoom('armor'), "#O2 Failed  isObjectInRoom")
 
    #O4
    def test_ObjectsVisible(self):
        self.assertFalse(dm.isObjectVisible('lockpick'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('mushrooms'), "#O4  Failed  ObjectsVisible")
        dm.setOnObjectsVisible('metal shelves', True)
        self.assertTrue(dm.isObjectVisible('lockpick'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('mushrooms'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('scroll'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('bottle of gatorade'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('bottleopener'), "#O4  Failed  ObjectsVisible")
        dm.setOnObjectsVisible('desk', True)
        self.assertFalse(dm.isObjectVisible('scroll'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('bottle of gatorade'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('bottleopener'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getOnObjectsVisible('desk'), ['bottle of gatorade', 'bottleopener'], "#O4  Failed  ObjectsVisible")
        dm.setInsideObjectsVisible('desk', True)
        self.assertTrue(dm.isObjectVisible('scroll'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('bottle of gatorade'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('bottleopener'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getInsideObjectsVisible('desk'), ['scroll'], "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('wooden lever'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getBehindObjectsVisible(''), [], "#O4  Failed  ObjectsVisible")
        dm.setBehindObjectsVisible('wooden shelves', True)
        self.assertTrue(dm.isObjectVisible('wooden lever'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getBehindObjectsVisible('wooden shelves'), ['wooden lever'], "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('book of locks'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('human skeleton'), "#O4  Failed  ObjectsVisible")
        dm.setUnderObjectsVisible('mattress', True)
        self.assertTrue(dm.isObjectVisible('book of locks'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('human skeleton'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getUnderObjectsVisible('mattress'), ['book of locks'], "#O4  Failed  ObjectsVisible")
        dm.setOnObjectsVisible('mattress', True)
        self.assertTrue(dm.isObjectVisible('book of locks'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('human skeleton'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getOnObjectsVisible('mattress'), ['human skeleton'], "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('axe'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('magical ring'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getUnderObjectsVisible('altar'), [], "#O4  Failed  ObjectsVisible")
        dm.setAboveObjectsVisible('altar', True)
        self.assertTrue(dm.isObjectVisible('axe'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('magical ring'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getAboveObjectsVisible('altar'), ['axe'], "#O4  Failed  ObjectsVisible")
        dm.setOnObjectsVisible('altar', True)
        self.assertTrue(dm.isObjectVisible('axe'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('magical ring'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getOnObjectsVisible('altar'), ['magical ring'], "#O4  Failed  ObjectsVisible")
    #O5
    def test_setObjectUnlocked(self):
        self.assertFalse(dm.isObjectUnlocked('safe'), "#O5  Failed ObjectUnlocked")
        dm.setObjectUnlocked('safe', True)
        self.assertTrue(dm.isObjectUnlocked('safe'), "#O5  Failed ObjectUnlocked")
    #O6
    def test_changeLocation(self):
        dm.changeLocation('wooden lever')
        self.assertEqual(dm.getPlayerLocation(), 'ct', "#O6  Failed changeLocation")
        dm.changeLocation('iron lever')
        self.assertEqual(dm.getPlayerLocation(), 'bd', "#O6  Failed changeLocation") 
        dm.changeLocation('trapdoor')
        self.assertEqual(dm.getPlayerLocation(), 'tr', "#O6  Failed changeLocation")     
    #O7 
    def test_setObjectRead(self):
        self.assertFalse(dm.isObjectRead('note'), "#07  Failed ObjectRead")
        dm.setObjectRead('note', True)
        self.assertTrue(dm.isObjectRead('note'), "#07  Failed ObjectRead")
    #O8 
    def test_setObjectEquipped(self):
        dm.setObjectEquipped('armor', False)
        self.assertFalse(dm.isObjectEquipped('armor'), "#08  Failed ObjectEquipped")
        dm.setObjectEquipped('armor', True)
        self.assertTrue(dm.isObjectEquipped('armor'), "#08  Failed ObjectEquipped")     
    #O9 
    def test_setObjectLighted(self):
        self.assertFalse(dm.isObjectLighted('broken lantern'), "#09  Failed ObjectLighted")
        dm.setObjectLighted('broken lantern', True)
        self.assertTrue(dm.isObjectLighted('broken lantern'), "#09  Failed ObjectLighted")       
    #O10
    def test_isObjectEquippable(self):  
        dm.clearInventoryObjects() 
        self.assertFalse(dm.isObjectEquippable('green apple'),  "#O10  Failed isObjectEquippable")
        self.assertTrue(dm.isObjectEquippable('axe'),  "#O10  Failed isObjectEquippable")
        self.assertTrue(dm.isObjectEquippable('machete'),  "#O10  Failed isObjectEquippable")

    #O11
    def test_setObjectKeyObject(self):
        self.assertEqual(dm.getObjectKeyObject('safe'), 'lock',  "#O11  Failed setObjectKeyObject")
        dm.setObjectKeyObject('safe', '')
        self.assertEqual(dm.getObjectKeyObject('safe'), '',  "#O11  Failed setObjectKeyObject")
    #O12
    def test_getEquippedObjects(self):
        dm.clearInventoryObjects()
        self.assertItemsEqual(dm.getEquippedObjects(), [], "#O12  Failed getEquippedObjects")
        dm.addInventoryObject('armor')
        dm.addInventoryObject('green apple')
        dm.addInventoryObject('machete')
        self.assertItemsEqual(dm.getEquippedObjects(), [], "#O12  Failed getEquippedObjects")
        dm.setObjectEquipped('armor', True)
        self.assertItemsEqual(dm.getEquippedObjects(), ['armor'], "#O12  Failed getEquippedObjects")
        dm.setObjectEquipped('machete', True)
        self.assertItemsEqual(dm.getEquippedObjects(), ['armor', 'machete'], "#O12  Failed getEquippedObjects")
        dm.setObjectEquipped('armor', False)
        self.assertItemsEqual(dm.getEquippedObjects(), ['machete'], "#O12  Failed getEquippedObjects")
  
  
   
class GoToRoom(unittest.TestCase):
    data = [ {'room':'ap',   'exit':'west',                   'expected':'wl'}, 
             {'room':'ap',   'exit':'oblivion gate',          'expected':'wl'},
             {'room':'ar',   'exit':'north',                  'expected':'hw'},
             {'room':'ar',   'exit':'winder stairs',          'expected':'hw'},
             {'room':'ar',   'exit':'east',                   'expected':'jl'},
             {'room':'ar',   'exit':'rusting iron door',      'expected':'jl'},
             {'room':'ar',   'exit':'south',                  'expected':'sq'},
             {'room':'ar',   'exit':'solid metal door',       'expected':'sq'},   
             {'room':'bd',   'exit':'east',                   'expected':'sq'},
             {'room':'bd',   'exit':'old wooden door',        'expected':'sq'},
             {'room':'bh',   'exit':'north',                  'expected':'kt'},
             {'room':'bh',   'exit':'splintered double doors','expected':'kt'},
             {'room':'bh',   'exit':'east',                   'expected':'hw'},
             {'room':'bh',   'exit':'monstrous archway',      'expected':'hw'},
             {'room':'ca',   'exit':'south',                  'expected':'pw'},
             {'room':'ca',   'exit':'rolling shutter door',   'expected':'pw'},
             {'room':'ca',   'exit':'east',                   'expected':'kt'},
             {'room':'ca',   'exit':'smoky glazed doors',     'expected':'kt'},
             {'room':'ce',   'exit':'south',                  'expected':'ot'},
             {'room':'ce',   'exit':'corrugated steel door',  'expected':'ot'},
             {'room':'ce',   'exit':'north',                  'expected':'pw'},
             {'room':'ce',   'exit':'long dark tunnel',       'expected':'pw'},
             {'room':'cl',   'exit':'west',                   'expected':'jl'},
             {'room':'cl',   'exit':'creaking cell door',     'expected':'jl'},
             {'room':'hw',   'exit':'west',                   'expected':'bh'},
             {'room':'hw',   'exit':'monstrous archway',      'expected':'bh'},
             {'room':'hw',   'exit':'east',                   'expected':'wl'},
             {'room':'hw',   'exit':'bell archway',           'expected':'wl'},
             {'room':'hw',   'exit':'south',                  'expected':'ar'},
             {'room':'hw',   'exit':'winder stairs',          'expected':'ar'},
             {'room':'jl',   'exit':'west',                   'expected':'ar'},
             {'room':'jl',   'exit':'rusting iron door',      'expected':'ar'},       
             {'room':'jl',   'exit':'east',                   'expected':'cl'},
             {'room':'jl',   'exit':'creaking cell door',     'expected':'cl'},          
             {'room':'kt',   'exit':'west',                   'expected':'ca'},
             {'room':'kt',   'exit':'smoky glazed doors',     'expected':'ca'},   
             {'room':'kt',   'exit':'east',                   'expected':'sr'},
             {'room':'kt',   'exit':'swinging door',          'expected':'sr'}, 
             {'room':'kt',   'exit':'south',                  'expected':'bh'},
             {'room':'kt',   'exit':'splintered double doors','expected':'bh'},
             {'room':'ot',   'exit':'north',                  'expected':'ce'},
             {'room':'ot',   'exit':'corrugated steel door',  'expected':'ce'},
             {'room':'pw',   'exit':'south',                  'expected':'ce'},
             {'room':'pw',   'exit':'long dark tunnel',       'expected':'ce'},
             {'room':'pw',   'exit':'north',                  'expected':'ca'},
             {'room':'pw',   'exit':'rolling shutter door',     'expected':'ca'}, 
             {'room':'sq',   'exit':'north',                  'expected':'ar'},
             {'room':'sq',   'exit':'solid metal door',       'expected':'ar'},
             {'room':'sq',   'exit':'west',                   'expected':'bd'},
             {'room':'sq',   'exit':'old wooden door',        'expected':'bd'},          
             {'room':'sr',   'exit':'west',                   'expected':'kt'},
             {'room':'sr',   'exit':'swinging door',          'expected':'kt'}, 
             {'room':'tr',   'exit':'west',                   'expected':'sr'},
             {'room':'tr',   'exit':'rusted spiral staircase','expected':'sr'},
             {'room':'wl',   'exit':'west',                   'expected':'hw'},
             {'room':'wl',   'exit':'bell archway',           'expected':'hw'},
             {'room':'wl',   'exit':'east',                   'expected':'ap'},
             {'room':'wl',   'exit':'obilivion gate',         'expected':'ap'}]
             
    def test_GoToRoom(self):
        for i in self.data:
            dm.setPlayerLocation(i['room'])
            dm.movePlayer(i['exit'])
            self.assertEqual(dm.getPlayerLocation(),  i['expected'],  "Failed: " + i['exit'])
 


if __name__ == '__main__':
	unittest.main()
