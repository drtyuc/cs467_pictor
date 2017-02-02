from DMT.GameData import DataManager
import unittest

dm = DataManager()
dm.loadNewGame()


class Player(unittest.TestCase):
    #P1  
    def test_adjustPlayerHealth(self):
        dm.adjustPlayerHealth('apple1')
        self.assertEqual(dm.getPlayerHealth(), 115, "#P1: FAILED adjustPlayerHealth")
    #P2
    def test_isPlayerVisible(self):
        dm.setPlayerVisible(True)
        self.assertTrue(dm.isPlayerVisible(), "#P2  FAILED isPlayerVisible")
    #P3
    def test_setPlayerVisible(self):
        dm.setPlayerVisible(False)
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
        dm.movePlayer('Exit going north')
        self.assertEqual(dm.getPlayerLocation(), 'pw', "#P7  FAILED movePlayer2")


class Inventory(unittest.TestCase):       
    #I1    
    def test_InventoryCapacity(self):
        dm.setInventoryCapacity(150)
        self.assertEqual(dm.getInventoryCapacity(), 150,  "1#I1  FAILED InventoryCapacity")
    #I2
    def test_addInventoryObject(self):
        olist = ['armor1', 'sword1', 'bottle1']
        dm.clearInventoryObjects()
        dm.addInventoryObject("armor1")
        dm.addInventoryObject("sword1")
        dm.addInventoryObject("bottle1")
        self.assertItemsEqual(dm.getInventoryObjects(), olist,  "#I2  FAILED addInventoryObject")
        self.assertEqual(dm.getObjectLocation('bottle1'), 'inventory', "#I2   FAILED addInventoryObject")
    #I3
    def test_removeInventoryObject(self):
        olist = ['armor1', 'bottle1']
        dm.clearInventoryObjects()
        dm.addInventoryObject("armor1")
        dm.addInventoryObject("sword1")
        dm.addInventoryObject("bottle1")
        dm.removeInventoryObject("sword1")
        self.assertItemsEqual(dm.getInventoryObjects(), olist,  "#I3  FAILED removeInventoryObject")
      
    #I4
    def test_getInventoryWeight(self):
        dm.clearInventoryObjects()       
        dm.addInventoryObject("armor1")
        dm.addInventoryObject("apple1")
        self.assertEqual(dm.getInventoryWeight(),  85, "#I4  FAILED getInventoryWeight")
    #I5
    def test_isSpaceInInventory1(self):
        dm.clearInventoryObjects()
        dm.addInventoryObject("armor1")
        self.assertTrue(dm.isSpaceInInventory("apple1"), "#I5  FAILED  isSpaceInInventory")
    #I6
    def test_isSpaceInInventory2(self):
        dm.clearInventoryObjects() 
        dm.addInventoryObject("armor1")
        self.assertFalse(dm.isSpaceInInventory("safe1"), "#I6  FAILED  isSpaceInInventory")
 
 
 
class Rooms(unittest.TestCase):  
    #R1
    def test_getRoomNames(self):
        rlist = ['ap', 'ar', 'bd', 'bh', 'ca', 'ce', 'cl', 'ct', 'hw', 'jl', 'kt', 'ot',
                 'pw', 'sq', 'sr', 'tr', 'wl']
        self.assertItemsEqual(dm.getRoomNames(), rlist,  "#R1  FAILED  getRoomNames")
    #R2
    def test_getRoomLongDescription(self):
        dm.setPlayerLocation('kt')
        self.assertEqual(dm.getRoomLongDescription(), "Kitchen Long Description", "#R2  Failed getRoomLongDescription")
    #R3
    def test_getRoomShortDescription(self):
        dm.setPlayerLocation('kt')
        self.assertEqual(dm.getRoomShortDescription(), "Kitchen Short Description", "#R3  Failed getRoomShortDescription")
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
        dm.setRoomLighted(True)
        self.assertTrue(dm.isRoomLighted(), "#R6  Failed  isRoomLighted")
    #R7
    def test_setRoomLighted(self):
        dm.setPlayerLocation('kt')
        dm.setRoomLighted(False)
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
        self.assertEqual(dm.getExitLongDescription('kt1'), "KT1 Long Description", "#E2 Failed  getExitLongDesciption")
    #E3
    def test_getExitShortDescription(self):
        self.assertEqual(dm.getExitShortDescription('kt1'), "Exit going west", "#E3 Failed  getExitShortDesciption")
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
        self.assertTrue(dm.isExitInRoom('Exit going south'), "#E8  Failed isExitInRoom")
        self.assertFalse(dm.isExitInRoom('bh1'), "#E8  Failed isExitInRoom")
        self.assertFalse(dm.isExitInRoom('west'), "#E8  Failed isExitInRoom")
        self.assertFalse(dm.isExitInRoom('Exit going west'), "#E8  Failed isExitInRoom")
    #E9
    def test_isExitKeyInInventory(self):
        dm.clearInventoryObjects()
        self.assertFalse(dm.isExitKeyInInventory('ce1'), "#E9  Failed  isExitKeyInInventory")
        dm.addInventoryObject('key1')
        self.assertTrue(dm.isExitKeyInInventory('ce1'), "#E9  Failed  isExitKeyInInventory")
        self.assertTrue(dm.isExitKeyInInventory('ce2'), "#E9  Failed  isExitKeyInInventory")        
        
        
    
class Objects(unittest.TestCase):
    #O1
    def test_isObjectInInventory(self):
        dm.clearInventoryObjects()
        dm.addInventoryObject('apple1')
        self.assertTrue(dm.isObjectInInventory('apple1'), "#O1 Failed  isObjectInInventory")
        self.assertFalse(dm.isObjectInInventory('armor1'), "#O1 Failed  isObjectInInventory")
    #O2
    def test_isObjectInRoom(self):
        dm.setPlayerLocation('ap')
        dm.clearRoomObjects()
        dm.addRoomObject('apple1')
        self.assertTrue(dm.isObjectInRoom('apple1'), "#O2 Failed  isObjectInRoom")
        self.assertFalse(dm.isObjectInRoom('armor1'), "#O2 Failed  isObjectInRoom")
    #O3
    def test_isObjectKeyInInventory(self):
        dm.clearInventoryObjects()
        self.assertFalse(dm.isObjectKeyInInventory('safe1'), "#O3  Failed  isObjectKeyInInventory")
        dm.addInventoryObject('note1')
        self.assertTrue(dm.isObjectKeyInInventory('safe1'), "#O3  Failed  isObjectKeyInInventory")
        self.assertTrue(dm.isObjectKeyInInventory('apple1'), "#O3  Failed  isObjectKeyInInventory")
    #O4
    def test_ObjectsVisible(self):
        self.assertFalse(dm.isObjectVisible('lockpick1'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('mushrooms1'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getOnObjectsVisible('shelf1'), [], "#O4  Failed  ObjectsVisible")
        dm.setOnObjectsVisible('shelf1', True)
        self.assertTrue(dm.isObjectVisible('lockpick1'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('mushrooms1'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getOnObjectsVisible('shelf1'), ['lockpick1', 'mushrooms1'], "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('scroll1'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('bottle2'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('bottleopener1'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getOnObjectsVisible('desk1'), [], "#O4  Failed  ObjectsVisible")
        dm.setOnObjectsVisible('desk1', True)
        self.assertFalse(dm.isObjectVisible('scroll1'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('bottle2'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('bottleopener1'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getOnObjectsVisible('desk1'), ['bottle2', 'bottleopener1'], "#O4  Failed  ObjectsVisible")
        dm.setInsideObjectsVisible('desk1', True)
        self.assertTrue(dm.isObjectVisible('scroll1'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('bottle2'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('bottleopener1'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getInsideObjectsVisible('desk1'), ['scroll1'], "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('lever1'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getBehindObjectsVisible(''), [], "#O4  Failed  ObjectsVisible")
        dm.setBehindObjectsVisible('shelf3', True)
        self.assertTrue(dm.isObjectVisible('lever1'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getBehindObjectsVisible('shelf3'), ['lever1'], "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('book2'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('bones3'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getUnderObjectsVisible('mattress1'), [], "#O4  Failed  ObjectsVisible")
        dm.setUnderObjectsVisible('mattress1', True)
        self.assertTrue(dm.isObjectVisible('book2'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('bones3'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getUnderObjectsVisible('mattress1'), ['book2'], "#O4  Failed  ObjectsVisible")
        dm.setOnObjectsVisible('mattress1', True)
        self.assertTrue(dm.isObjectVisible('book2'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('bones3'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getOnObjectsVisible('mattress1'), ['bones3'], "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('axe1'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('ring1'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getUnderObjectsVisible('altar1'), [], "#O4  Failed  ObjectsVisible")
        dm.setAboveObjectsVisible('altar1', True)
        self.assertTrue(dm.isObjectVisible('axe1'), "#O4  Failed  ObjectsVisible")
        self.assertFalse(dm.isObjectVisible('ring1'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getAboveObjectsVisible('altar1'), ['axe1'], "#O4  Failed  ObjectsVisible")
        dm.setOnObjectsVisible('altar1', True)
        self.assertTrue(dm.isObjectVisible('axe1'), "#O4  Failed  ObjectsVisible")
        self.assertTrue(dm.isObjectVisible('ring1'), "#O4  Failed  ObjectsVisible")
        self.assertItemsEqual(dm.getOnObjectsVisible('altar1'), ['ring1'], "#O4  Failed  ObjectsVisible")
    #O5
    def test_setObjectUnlocked(self):
        self.assertFalse(dm.isObjectUnlocked('safe1'), "#O5  Failed ObjectUnlocked")
        dm.setObjectUnlocked('safe1', True)
        self.assertTrue(dm.isObjectUnlocked('safe1'), "#O5  Failed ObjectUnlocked")
    #O6
    def test_changeLocation(self):
        dm.changeLocation('lever1')
        self.assertEqual(dm.getPlayerLocation(), 'ct', "#O6  Failed changeLocation")
        dm.changeLocation('lever2')
        self.assertEqual(dm.getPlayerLocation(), 'bd', "#O6  Failed changeLocation") 
        dm.changeLocation('trapdoor1')
        self.assertEqual(dm.getPlayerLocation(), 'tr', "#O6  Failed changeLocation")     
    #O7 
    def test_setObjectRead(self):
        self.assertFalse(dm.isObjectRead('note1'), "#07  Failed ObjectRead")
        dm.setObjectRead('note1', True)
        self.assertTrue(dm.isObjectRead('note1'), "#07  Failed ObjectRead")
    #O7 
    def test_setObjectEquipped(self):
        self.assertFalse(dm.isObjectEquipped('armor1'), "#07  Failed ObjectEquipped")
        dm.setObjectEquipped('armor1', True)
        self.assertTrue(dm.isObjectEquipped('armor1'), "#07  Failed ObjectEquipped")     
    #O8 
    def test_setObjectLighted(self):
        self.assertFalse(dm.isObjectLighted('lantern1'), "#08  Failed ObjectLighted")
        dm.setObjectLighted('lantern1', True)
        self.assertTrue(dm.isObjectLighted('lantern1'), "#08  Failed ObjectLighted")         
       
if __name__ == '__main__':
	unittest.main()
