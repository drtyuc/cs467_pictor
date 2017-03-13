from DMT.GameData import DataManager
import unittest

dm = DataManager()
dm.loadNewGame()
dep = dm.getDependencies()

def getDependencyIndex(cmd):
    index = 0;
    for i in dep['commands']:
        if i['tuple'] == cmd:
            return index
        index += 1
    return -1 


class Drink(unittest.TestCase):

    dm = DataManager()
    dm.loadNewGame()
    
    data = [ { "cmd":"drink bottle of gatorade",    "obj":"bottle of gatorade", "target": 85 },
             { "cmd":"drink bottle of water",       "obj":"bottle of water" ,   "target": 75} ]
             
    def checkDependency(self, method, obj, expect):
        if method == 'isObjectInInventory()':
            return self.dm.isObjectInInventory(obj) == expect
        if method == 'isObjectDrinkable()':
            return self.dm.isObjectDrinkable(obj) == expect     
            
    def takeAction(self, method, obj, state):
        if method == 'removeInventoryObject()':
            self.dm.removeInventoryObject(obj, state)
        if method == 'adjustPlayerHealth()':
            self.dm.adjustPlayerHealth(obj, state)         
    
    def test_DrinkObjects(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.addInventoryObject(i['obj'])
            d = dep['commands'][index]['dependencies']
            for j in [0,1]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            self.dm.setPlayerHealth(50)
            for k in [0,1]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertEqual(self.dm.getPlayerHealth(), i['target'])
            self.assertFalse(self.dm.isObjectInInventory(a[0]['object']))
            self.assertFalse(self.dm.isObjectInRoom(a[0]['object']))
            self.assertFalse(self.dm.isObjectInInventory(a[1]['object']))
            self.assertFalse(self.dm.isObjectInRoom(a[1]['object']))
            
         
class Drop(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    def checkDependency(self, method, obj, expect):
        if method == 'isObjectInInventory()':
            return self.dm.isObjectInInventory(obj) == expect
        if method == 'isObjectEquipped()':
            return self.dm.isObjectEquipped(obj) == expect     
            
    def takeAction(self, method, obj, state):
        if method == 'removeInventoryObject()':
            self.dm.removeInventoryObject(obj, state)
        if method == 'addRoomObject()':
            self.dm.addRoomObject(obj, state)
    
    data = [ { "cmd":"drop armor",               "equipped":True,   "obj":"armor" },
             { "cmd":"drop axe",                 "equipped":True,   "obj":"axe" },
             { "cmd":"drop book of locks",       "equipped":False,  "obj":"book of locks" },
             { "cmd":"drop book of spells",      "equipped":False,  "obj":"book of spells" },
             { "cmd":"drop bottle of water",     "equipped":False,  "obj":"bottle of water" },
             { "cmd":"drop bottle of gatorade",  "equipped":False,  "obj":"bottle of gatorade" },
             { "cmd":"drop bottleopener",        "equipped":False,  "obj":"bottleopener" },
             { "cmd":"drop brass lantern",       "equipped":False,  "obj":"brass lantern" },
             { "cmd":"drop broken lantern",      "equipped":False,  "obj":"broken lantern" },
             { "cmd":"drop cloak",               "equipped":True,   "obj":"cloak" },
             { "cmd":"drop earthenware",         "equipped":False,  "obj":"earthenware" },
             { "cmd":"drop fine china",          "equipped":False,  "obj":"fine china" },
             { "cmd":"drop gem",                 "equipped":True,   "obj":"gem" },
             { "cmd":"drop golden key",          "equipped":False,  "obj":"golden key" },
             { "cmd":"drop green apple",         "equipped":False,  "obj":"green apple" },
             { "cmd":"drop helmet",              "equipped":True,   "obj":"helmet" },
             { "cmd":"drop kitchen knife",       "equipped":True,   "obj":"kitchen knife" },
             { "cmd":"drop lockpick",            "equipped":False,  "obj":"lockpick" },
             { "cmd":"drop machete",             "equipped":True,   "obj":"machete" },
             { "cmd":"drop magical ring",        "equipped":True,   "obj":"magical ring" },
             { "cmd":"drop matches",             "equipped":False,  "obj":"matches" },
             { "cmd":"drop mushrooms",           "equipped":False,  "obj":"mushrooms" },
             { "cmd":"drop note",                "equipped":False,  "obj":"note" },
             { "cmd":"drop red apple",           "equipped":False,  "obj":"red apple" },
             { "cmd":"drop sabre",               "equipped":True,   "obj":"sabre" },
             { "cmd":"drop scroll",              "equipped":False,  "obj":"scroll" },
             { "cmd":"drop shale rocks",         "equipped":False,  "obj":"shale rocks" },
             { "cmd":"drop slate rocks",         "equipped":False,  "obj":"slate rocks" },
             { "cmd":"drop stoneware",           "equipped":False,  "obj":"stoneware" },
             { "cmd":"drop treasure",            "equipped":False,  "obj":"treasure" },
             { "cmd":"drop warhammer",           "equipped":False,  "obj":"warhammer" } ]
 
       
    def test_DropObjects(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.addInventoryObject(i['obj'])
            if i['equipped']:
                self.dm.setObjectEquipped(i['obj'], False)
            d = dep['commands'][index]['dependencies']
            self.assertTrue(self.checkDependency(d[0]['method'], d[0]['object'], d[0]['expect']))
            if i['equipped']:
                self.assertTrue(self.checkDependency(d[1]['method'], d[1]['object'], d[1]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0,1]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertFalse(self.dm.isObjectInInventory(a[0]['object']))
            self.assertTrue(self.dm.isObjectInRoom(a[0]['object']))      
            self.assertFalse(self.dm.isObjectInInventory(a[1]['object']))
            self.assertTrue(self.dm.isObjectInRoom(a[1]['object'])) 
            
            
class Eat(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [ { "cmd":"eat green apple",    "obj":"green apple",  "target": 65  },
             { "cmd":"eat mushrooms",      "obj":"mushrooms",    "target": 80  },
             { "cmd":"eat red apple",      "obj":"red apple",    "target": 65  } ]
             
    def checkDependency(self, method, obj, expect):
        if method == 'isObjectInInventory()':
            return self.dm.isObjectInInventory(obj) == expect
        if method == 'isObjectEdible()':
            return self.dm.isObjectEdible(obj) == expect     
            
    def takeAction(self, method, obj, state):
        if method == 'removeInventoryObject()':
            self.dm.removeInventoryObject(obj, state)
        if method == 'adjustPlayerHealth()':
            self.dm.adjustPlayerHealth(obj, state) 
    
    def test_EatObjects(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.addInventoryObject(i['obj'])
            d = dep['commands'][index]['dependencies']
            for j in [0,1]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            self.dm.setPlayerHealth(50)
            for k in [0,1]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertEqual(self.dm.getPlayerHealth(), i['target'])
            self.assertFalse(self.dm.isObjectInInventory(a[0]['object']))
            self.assertFalse(self.dm.isObjectInRoom(a[0]['object'])) 
        

class Equip1(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [ { "cmd":"equip axe",    "obj":"axe" },
             { "cmd":"equip kitchen knife", "obj":"kitchen knife" },
             { "cmd":"equip machete", "obj":"machete" },
             { "cmd":"equip sabre", "obj":"sabre" },
             { "cmd":"equip warhammer", "obj":"warhammer" } ]
    
    def checkDependency(self, method, obj, expect):
        if method == 'isObjectInInventory()':
            return self.dm.isObjectInInventory(obj) == expect
        if method == 'isObjectEquipped()':
            return self.dm.isObjectEquipped(obj) == expect  
        if method == 'isObjectEquippable()':
            return self.dm.isObjectEquippable(obj) == expect   
            
    def takeAction(self, method, obj, state):
        if method == 'setObjectEquipped()':
            self.dm.setObjectEquipped(obj, state)
    
    
    def test_Equip1Objects(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.addInventoryObject(i['obj'])
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertTrue(self.dm.isObjectEquipped(a[0]['object'])) 
            self.dm.setObjectEquipped(a[0]['object'], False)
        

class Equip2(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [ { "cmd":"equip armor",  "obj":"armor", },
             { "cmd":"equip cloak",  "obj":"cloak" },
             { "cmd":"equip helmet", "obj":"helmet" },
             { "cmd":"equip magical ring", "obj":"magical ring" } ]
    
    def checkDependency(self, method, obj, expect):
        if method == 'isObjectInInventory()':
            return self.dm.isObjectInInventory(obj) == expect
        if method == 'isObjectEquipped()':
            return self.dm.isObjectEquipped(obj) == expect  
            
    def takeAction(self, method, obj, state):
        if method == 'setObjectEquipped()':
            self.dm.setObjectEquipped(obj, state)
    
    
    def test_Equip2Objects(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.addInventoryObject(i['obj'])
            d = dep['commands'][index]['dependencies']
            for j in [0,1]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertTrue(self.dm.isObjectEquipped(a[0]['object'])) 


class GoDirectionUnlocked(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [ { "cmd":"eat green apple",    "obj":"green apple",  "target": 115  },
             { "cmd":"eat mushrooms",      "obj":"mushrooms",    "target": 130  },
             { "cmd":"eat red apple",      "obj":"red apple",    "target": 115  } ]
             
    def checkDependency(self, method, obj, expect):
        if method == 'isExitInRoom()':
            return self.dm.isExitInRoom(obj) == expect
        if method == 'isExitVisible()':
            return self.dm.isExitVisible(obj) == expect  
        if method == 'isExitUnlocked()':
            return self.dm.isExitUnlocked(obj) == expect   
            
    def takeAction(self, method, obj, state):
        if method == 'movePlayer()':
            self.dm.movePlayer(obj, state)
            
            
    data = [ { "cmd":"go north",  "room":"ce",  "target":"pw" },
             { "cmd":"go north",  "room":"ot",  "target":"ce" },
             { "cmd":"go south",  "room":"pw",  "target":"ce" },
             { "cmd":"go north",  "room":"pw",  "target":"ca" },
             { "cmd":"go south",  "room":"ca",  "target":"pw" },
             { "cmd":"go east",   "room":"ca",  "target":"kt" },
             { "cmd":"go west",   "room":"kt",  "target":"ca" },
             { "cmd":"go east",   "room":"kt",  "target":"sr" },
             { "cmd":"go south",  "room":"kt",  "target":"bh" },
             { "cmd":"go west",   "room":"sr",  "target":"kt" },
             { "cmd":"go west",   "room":"tr",  "target":"sr" },
             { "cmd":"go north",  "room":"bh",  "target":"kt" },
             { "cmd":"go east",   "room":"bh",  "target":"hw" },
             { "cmd":"go west",   "room":"hw",  "target":"bh" },
             { "cmd":"go east",   "room":"hw",  "target":"wl" },
             { "cmd":"go south",  "room":"hw",  "target":"ar" },
             { "cmd":"go west",   "room":"wl",  "target":"hw" },
             { "cmd":"go east",   "room":"wl",  "target":"ap" },
             { "cmd":"go west",   "room":"ap",  "target":"wl" },
             { "cmd":"go north",  "room":"ar",  "target":"hw" },
             { "cmd":"go east",   "room":"ar",  "target":"jl" },
             { "cmd":"go south",  "room":"ar",  "target":"sq" },
             { "cmd":"go west",   "room":"jl",  "target":"ar" },
             { "cmd":"go east",   "room":"jl",  "target":"cl" },
             { "cmd":"go west",   "room":"cl",  "target":"jl" },
             { "cmd":"go west",   "room":"sq",  "target":"bd" },
             { "cmd":"go north",  "room":"sq",  "target":"ar" },
             { "cmd":"go east",   "room":"bd",  "target":"sq" },
             { "cmd":"go oblivion gate",   "room":"ap",  "target":"wl" },
             { "cmd":"go winder stairs",   "room":"ar",  "target":"hw" },
             { "cmd":"go rusting iron door",   "room":"ar",  "target":"jl" },
             { "cmd":"go solid metal door",   "room":"ar",  "target":"sq" },
             { "cmd":"go old wooden door",   "room":"bd",  "target":"sq" },
             { "cmd":"go splintered double doors",   "room":"bh",  "target":"kt" },
             { "cmd":"go monstrous archway",   "room":"bh",  "target":"hw" },
             { "cmd":"go rolling shutter door",   "room":"ca",  "target":"pw" },
             { "cmd":"go smoky glazed doors",   "room":"ca",  "target":"kt" },
             { "cmd":"go long dark tunnel",   "room":"ce",  "target":"pw" },
             { "cmd":"go creaking cell door",   "room":"cl",  "target":"jl" },
             { "cmd":"go monstrous archway",   "room":"hw",  "target":"bh" },
             { "cmd":"go bell archway",   "room":"hw",  "target":"wl" },
             { "cmd":"go winder stairs",   "room":"hw",  "target":"ar" },
             { "cmd":"go corrugated steel door",   "room":"ot",  "target":"ce" },
             { "cmd":"go rusting iron door",   "room":"jl",  "target":"ar" },
             { "cmd":"go creaking cell door",   "room":"jl",  "target":"cl" },
             { "cmd":"go smoky glazed doors",   "room":"kt",  "target":"ca" },
             { "cmd":"go swinging door",   "room":"kt",  "target":"sr" },
             { "cmd":"go splintered double doors",   "room":"kt",  "target":"bh" },
             { "cmd":"go long dark tunnel",   "room":"pw",  "target":"ce" },
             { "cmd":"go rolling shutter door",   "room":"pw",  "target":"ca" },
             { "cmd":"go solid metal door",   "room":"sq",  "target":"ar" },
             { "cmd":"go old wooden door",   "room":"sq",  "target":"bd" },
             { "cmd":"go swinging door",   "room":"sr",  "target":"kt" },
             { "cmd":"go rusted spiral staircase",   "room":"tr",  "target":"sr" },
             { "cmd":"go bell archway",   "room":"wl",  "target":"hw" },
             { "cmd":"go oblivion gate",   "room":"wl",  "target":"ap" },
             { "cmd":"north",  "room":"ce",  "target":"pw" },
             { "cmd":"north",  "room":"ot",  "target":"ce" },
             { "cmd":"south",  "room":"pw",  "target":"ce" },
             { "cmd":"north",  "room":"pw",  "target":"ca" },
             { "cmd":"south",  "room":"ca",  "target":"pw" },
             { "cmd":"east",   "room":"ca",  "target":"kt" },
             { "cmd":"west",   "room":"kt",  "target":"ca" },
             { "cmd":"east",   "room":"kt",  "target":"sr" },
             { "cmd":"south",  "room":"kt",  "target":"bh" },
             { "cmd":"west",   "room":"sr",  "target":"kt" },
             { "cmd":"west",   "room":"tr",  "target":"sr" },
             { "cmd":"north",  "room":"bh",  "target":"kt" },
             { "cmd":"east",   "room":"bh",  "target":"hw" },
             { "cmd":"west",   "room":"hw",  "target":"bh" },
             { "cmd":"east",   "room":"hw",  "target":"wl" },
             { "cmd":"south",  "room":"hw",  "target":"ar" },
             { "cmd":"west",   "room":"wl",  "target":"hw" },
             { "cmd":"east",   "room":"wl",  "target":"ap" },
             { "cmd":"west",   "room":"ap",  "target":"wl" },
             { "cmd":"north",  "room":"ar",  "target":"hw" },
             { "cmd":"east",   "room":"ar",  "target":"jl" },
             { "cmd":"south",  "room":"ar",  "target":"sq" },
             { "cmd":"west",   "room":"jl",  "target":"ar" },
             { "cmd":"east",   "room":"jl",  "target":"cl" },
             { "cmd":"west",   "room":"cl",  "target":"jl" },
             { "cmd":"west",   "room":"sq",  "target":"bd" },
             { "cmd":"north",  "room":"sq",  "target":"ar" },
             { "cmd":"east",   "room":"bd",  "target":"sq" },
             { "cmd":"oblivion gate",   "room":"ap",  "target":"wl" },
             { "cmd":"winder stairs",   "room":"ar",  "target":"hw" },
             { "cmd":"rusting iron door",   "room":"ar",  "target":"jl" },
             { "cmd":"solid metal door",   "room":"ar",  "target":"sq" },
             { "cmd":"old wooden door",   "room":"bd",  "target":"sq" },
             { "cmd":"splintered double doors",   "room":"bh",  "target":"kt" },
             { "cmd":"monstrous archway",   "room":"bh",  "target":"hw" },
             { "cmd":"rolling shutter door",   "room":"ca",  "target":"pw" },
             { "cmd":"smoky glazed doors",   "room":"ca",  "target":"kt" },
             { "cmd":"long dark tunnel",   "room":"ce",  "target":"pw" },
             { "cmd":"creaking cell door",   "room":"cl",  "target":"jl" },
             { "cmd":"monstrous archway",   "room":"hw",  "target":"bh" },
             { "cmd":"bell archway",   "room":"hw",  "target":"wl" },
             { "cmd":"winder stairs",   "room":"hw",  "target":"ar" },
             { "cmd":"corrugated steel door",   "room":"ot",  "target":"ce" },
             { "cmd":"rusting iron door",   "room":"jl",  "target":"ar" },
             { "cmd":"creaking cell door",   "room":"jl",  "target":"cl" },
             { "cmd":"smoky glazed doors",   "room":"kt",  "target":"ca" },
             { "cmd":"swinging door",   "room":"kt",  "target":"sr" },
             { "cmd":"splintered double doors",   "room":"kt",  "target":"bh" },
             { "cmd":"long dark tunnel",   "room":"pw",  "target":"ce" },
             { "cmd":"rolling shutter door",   "room":"pw",  "target":"ca" },
             { "cmd":"solid metal door",   "room":"sq",  "target":"ar" },
             { "cmd":"old wooden door",   "room":"sq",  "target":"bd" },
             { "cmd":"swinging door",   "room":"sr",  "target":"kt" },
             { "cmd":"rusted spiral staircase",   "room":"tr",  "target":"sr" },
             { "cmd":"bell archway",   "room":"wl",  "target":"hw" },
             { "cmd":"oblivion gate",   "room":"wl",  "target":"ap" }]

    def test_GoDirectionUnlocked(self):
        for i in self.data:
            index = getDependencyIndex(i["cmd"])
            d = dep['commands'][index]['dependencies']
            self.dm.setPlayerLocation(i["room"])
            for j in [0,1,2]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertEqual(self.dm.getPlayerLocation(), i['target'])


class GoDirectionLocked(unittest.TestCase):

    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"go south",  "room":"ce",  "target":"ot" },
              { "cmd":"go corrugated steel door",   "room":"ce",  "target":"ot" },
              { "cmd":"south",  "room":"ce",  "target":"ot" },
              { "cmd":"corrugated steel door",   "room":"ce",  "target":"ot" }]

    def checkDependency(self, method, obj, expect):
        if method == 'isExitInRoom()':
            return self.dm.isExitInRoom(obj) == expect
        if method == 'isExitVisible()':
            return self.dm.isExitVisible(obj) == expect  
        if method == 'isExitUnlocked()':
            return self.dm.isExitUnlocked(obj) == expect   
            
    def takeAction(self, method, obj, state):
        if method == 'movePlayer()':
            self.dm.movePlayer(obj, state)

    def test_GoDirectionUnlocked(self):
        for i in self.data:
            index = getDependencyIndex(i["cmd"])
            d = dep['commands'][index]['dependencies']
            self.dm.setPlayerLocation(i["room"])
            for j in [0,1]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            self.assertFalse(self.checkDependency(d[2]['method'], d[2]['object'], d[2]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])


class LayOn(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"lay on altar",     "obj":"altar",     "room":"tr", "target":50 }, 
              { "cmd":"lay on bearskin",  "obj":"bearskin",  "room":"sq", "target":82 }, 
              { "cmd":"lay on bunk bed",  "obj":"bunk bed",  "room":"sq", "target":90 },
              { "cmd":"lay on mattress",  "obj":"mattress",  "room":"cl", "target":75 },
              { "cmd":"lay on turkish rug",  "obj":"turkish rug",  "room":"sr", "target":75 },
              { "cmd":"lay on twin bed",  "obj":"twin bed",  "room":"bd", "target":100 },
              { "cmd":"lay on wool rug",  "obj":"wool rug",  "room":"hw", "target":80 }]

    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect
        if method == 'isObjectInRoom()':
            return self.dm.isObjectInRoom(obj) == expect  
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect   
        if method == 'isObjectLayable()':
            return self.dm.isObjectLayable(obj) == expect 
            
    def takeAction(self, method, obj, state):
        if method == 'adjustPlayerHealth()':
            self.dm.adjustPlayerHealth(obj, state)
    
    def test_LayOn(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            self.dm.setPlayerHealth(80)
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertEqual(self.dm.getPlayerHealth(), i['target'])    
  

class Light(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"light brass lantern",     "obj":"brass lantern",     "room":"sq"} ]


    def checkDependency(self, method, obj, expect):
        if method == 'isObjectInInventory()':
            return self.dm.isObjectInInventory(obj) == expect  
        if method == 'isObjectLighted()':
            return self.dm.isObjectLighted(obj) == expect   
        if method == 'isObjectLightable()':
            return self.dm.isObjectLightable(obj) == expect 
        if method == 'isObjectKeyInInventory()':
            return self.dm.isObjectKeyInInventory(obj) == expect
            
    def takeAction(self, method, obj, state):
        if method == 'setObjectLighted()':
            self.dm.setObjectLighted(obj, state)
    
    def test_Light(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.addInventoryObject(i['obj'])
            self.dm.addInventoryObject('matches')
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertTrue(self.dm.isObjectLighted(a[0]['object']))    
 

    
class LookAbove(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"look above altar",  "obj":"altar",  "room":"tr", "items":['axe']}]


    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect  
        if method == 'isObjectAccessible()':
            return self.dm.isObjectAccessible(obj) == expect   
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect 
        if method == 'isLookAbovePossible()':
            return self.dm.isLookAbovePossible(obj) == expect
            
    def takeAction(self, method, obj, state):
        if method == 'setAboveObjectsVisible()':
            self.dm.setAboveObjectsVisible(obj, state)
    
    def test_LookAbove(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            for n in i['items']:
                self.assertFalse(self.dm.isObjectVisible(n)) 
            d = dep['commands'][index]['dependencies']
            for j in [0,1, 2, 3]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            for m in i['items']:
                self.assertTrue(self.dm.isObjectVisible(m))    
   
class LookAt(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"look at altar",  "obj":"altar",  "room":"tr" },
              { "cmd":"look at sign",   "obj":"sign",   "room":"ot" } ]


    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect  
        if method == 'isObjectAccessible()':
            return self.dm.isObjectAccessible(obj) == expect   
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect 
            
    def takeAction(self, method, obj, state):
        if method == 'getObjectLongDescription()':
            self.dm.getObjectLongDescription(obj, state)
    
    def test_LookAt(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            self.dm.setObjectVisible(i['obj'], True)
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])

    
    
class LookBehind(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"look behind portrait",  "obj":"portrait",  "room":"ca", "items":['note']},
              { "cmd":"look behind wooden shelves",  "obj":"wooden shelves",  "room":"bd", "items":['wooden lever']}]


    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect  
        if method == 'isObjectAccessible()':
            return self.dm.isObjectAccessible(obj) == expect   
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect 
        if method == 'isLookBehindPossible()':
            return self.dm.isLookBehindPossible(obj) == expect
            
    def takeAction(self, method, obj, state):
        if method == 'setBehindObjectsVisible()':
            self.dm.setBehindObjectsVisible(obj, state)
    
    def test_LookBehind(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            for n in i['items']:
                self.assertFalse(self.dm.isObjectVisible(n)) 
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            for m in i['items']:
                self.assertTrue(self.dm.isObjectVisible(m))  


class LookInside(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"look inside armoire",  "obj":"armoire",  "room":"ct", "items":['cloak']},
              { "cmd":"look inside cedar trunk",  "obj":"cedar trunk",  "room":"bd", "items":['golden key']},
              { "cmd":"look inside desk",  "obj":"desk",  "room":"jl", "items":['scroll']},
              { "cmd":"look inside iron trunk",  "obj":"iron trunk",  "room":"tr", "items":['treasure']},
              { "cmd":"look inside safe",  "obj":"safe",  "room":"bd", "items":['gem']} ]
    

    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect  
        if method == 'isObjectAccessible()':
            return self.dm.isObjectAccessible(obj) == expect   
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect 
        if method == 'isObjectUnlocked()':
            return self.dm.isObjectUnlocked(obj) == expect 
        if method == 'isLookInsidePossible()':
            return self.dm.isLookInsidePossible(obj) == expect     
            
    def takeAction(self, method, obj, state):
        if method == 'setInsideObjectsVisible()':
            self.dm.setInsideObjectsVisible(obj, state)
    
    def test_LookInside(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            self.dm.setObjectUnlocked(i['obj'], True)
            for n in i['items']:
                self.assertFalse(self.dm.isObjectVisible(n)) 
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3,4]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            for m in i['items']:
                self.assertTrue(self.dm.isObjectVisible(m))  


class LookOn(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"look on altar",  "obj":"altar",  "room":"tr", "items":['magical ring']},
              { "cmd":"look on corner shelves",  "obj":"corner shelves",  "room":"wl", "items":['book of spells']},
              { "cmd":"look on desk",  "obj":"desk",  "room":"jl", "items":['bottle of gatorade', 'bottleopener']},
              { "cmd":"look on dining table",  "obj":"dining table",  "room":"bh", "items":['fine china', 'bottle of water']},
              { "cmd":"look on gateleg table",  "obj":"gateleg table",  "room":"ca", "items":['stoneware']},
              { "cmd":"look on high table",  "obj":"high table",  "room":"wl", "items":['broken lantern']},
              { "cmd":"look on kitchen table",  "obj":"kitchen table",  "room":"kt", "items":['matches', 'green apple', 'kitchen knife']},
              { "cmd":"look on mattress",  "obj":"mattress",  "room":"cl", "items":['human skeleton']},
              { "cmd":"look on metal shelves",  "obj":"metal shelves",  "room":"sr", "items":['lockpick', 'mushrooms']},
              { "cmd":"look on round table",  "obj":"round table",  "room":"sq", "items":['brass lantern']},
              { "cmd":"look on trestle table",  "obj":"trestle table",  "room":"ar", "items":['sabre', 'armor', 'warhammer', 'helmet']},
              { "cmd":"look on wooden shelves",  "obj":"wooden shelves",  "room":"bd", "items":[]}]
     


    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect  
        if method == 'isObjectAccessible()':
            return self.dm.isObjectAccessible(obj) == expect   
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect 
        if method == 'isLookOnPossible()':
            return self.dm.isLookOnPossible(obj) == expect 
            
    def takeAction(self, method, obj, state):
        if method == 'setOnObjectsVisible()':
            self.dm.setOnObjectsVisible(obj, state)
    
    def test_LookOn(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            for n in i['items']:
                self.assertFalse(self.dm.isObjectVisible(n)) 
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            for m in i['items']:
                self.assertTrue(self.dm.isObjectVisible(m))  



class LookUnder(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"look under bearskin",  "obj":"bearskin",  "room":"sq", "items":[]},
              { "cmd":"look under bunk bed",  "obj":"bunk bed",  "room":"sq", "items":['red apple']},
              { "cmd":"look under mattress",  "obj":"mattress",  "room":"cl", "items":['book of locks']},
              { "cmd":"look under turkish rug",  "obj":"turkish rug",  "room":"sr", "items":['trapdoor']},
              { "cmd":"look under wool rug",  "obj":"wool rug",  "room":"hw", "items":[]}]

    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect  
        if method == 'isObjectAccessible()':
            return self.dm.isObjectAccessible(obj) == expect   
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect 
        if method == 'isLookUnderPossible()':
            return self.dm.isLookUnderPossible(obj) == expect 
            
    def takeAction(self, method, obj, state):
        if method == 'setUnderObjectsVisible()':
            self.dm.setUnderObjectsVisible(obj, state)
    
    def test_LookUnder(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            for n in i['items']:
                self.assertFalse(self.dm.isObjectVisible(n)) 
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            for m in i['items']:
                self.assertTrue(self.dm.isObjectVisible(m))  



class Pull(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"pull wooden lever",  "obj":"wooden lever",  "room":"bd" , "target":"ct"},
              { "cmd":"pull trapdoor",  "obj":"trapdoor",  "room":"sr" , "target":"tr"}] 

    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect  
        if method == 'isObjectInRoom()':
            return self.dm.isObjectInRoom(obj) == expect   
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect 
        if method == 'isObjectPullable()':
            return self.dm.isObjectPullable(obj) == expect 
            
    def takeAction(self, method, obj, state):
        if method == 'changeLocation()':
            self.dm.changeLocation(obj, state)
    
    def test_Pull(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            self.dm.setObjectVisible(i['obj'], True)
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])  
            self.assertEqual(self.dm.getPlayerLocation(), i['target'])


class Push(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [{ "cmd":"push iron lever",  "obj":"iron lever",  "room":"ct" , "target":"bd"}]

    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect  
        if method == 'isObjectInRoom()':
            return self.dm.isObjectInRoom(obj) == expect   
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect 
        if method == 'isObjectPushable()':
            return self.dm.isObjectPushable(obj) == expect 
            
    def takeAction(self, method, obj, state):
        if method == 'changeLocation()':
            self.dm.changeLocation(obj, state)
    
    def test_Push(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            self.dm.setObjectVisible(i['obj'], True)
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])  
            self.assertEqual(self.dm.getPlayerLocation(), i['target'])


class Read1(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [{ "cmd":"read book of locks",  "obj":"book of locks",  "room":"ca" },
            { "cmd":"read book of spells", "obj":"book of spells",  "room":"ca" },
            { "cmd":"read scroll",  "obj":"scroll",  "room":"ca" },
            { "cmd":"read sign",  "obj":"sign",  "room":"ot" },
            { "cmd":"read slate of runes",  "obj":"slate of runes",  "room":"wl" }]

    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect  
        if method == 'isObjectInInventory()':
            return self.dm.isObjectInInventory(obj) == expect   
        if method == 'isObjectInRoom()':
            return self.dm.isObjectInRoom(obj) == expect 
        if method == 'isObjectReadable()':
            return self.dm.isObjectReadable(obj) == expect 
        if method == 'isObjectRead()':
            return self.dm.isObjectRead(obj) == expect 
            
    def takeAction(self, method, obj, state):
        if method == 'setObjectRead()':
            self.dm.setObjectRead(obj, state)
    
    def test_Read1(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            self.dm.addInventoryObject(i['obj'], True)
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])  
            self.assertTrue(self.dm.isObjectRead(a[0]['object']))



class Read2(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [{ "cmd":"read note",  "obj":"note",  "room":"ca" }]

    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect  
        if method == 'isObjectInInventory()':
            return self.dm.isObjectInInventory(obj) == expect   
        if method == 'isObjectInRoom()':
            return self.dm.isObjectInRoom(obj) == expect 
        if method == 'isObjectReadable()':
            return self.dm.isObjectReadable(obj) == expect 
        if method == 'isObjectRead()':
            return self.dm.isObjectRead(obj) == expect 
            
    def takeAction(self, method, obj, state):
        if method == 'setObjectRead()':
            self.dm.setObjectRead(obj, state)
        if method == 'setObjectUnlocked()':
            self.dm.setObjectUnlocked(obj, state)
    
    def test_Read2(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            self.dm.addInventoryObject(i['obj'], True)
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])  
            self.assertTrue(self.dm.isObjectRead(a[0]['object']))
    


class Sit(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"sit on bar stool",     "obj":"bar stool",     "room":"ca", "target":52 },
              { "cmd":"sit on bunk bed",  "obj":"bunk bed",  "room":"sq", "target":60},
              { "cmd":"sit on carver chair",  "obj":"carver chair",  "room":"jl", "target":55},
              { "cmd":"sit on milking stool",  "obj":"milking stool",  "room":"cl", "target":52 },
              { "cmd":"sit on rocking chair",  "obj":"rocking chair",  "room":"sq", "target":55 },
              { "cmd":"sit on twin bed",  "obj":"twin bed",  "room":"bd", "target":70 } ]

    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect  
        if method == 'isObjectInRoom()':
            return self.dm.isObjectInRoom(obj) == expect 
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect      
        if method == 'isObjectSitable()':
            return self.dm.isObjectSitable(obj) == expect 
            
    def takeAction(self, method, obj, state):
        if method == 'adjustPlayerHealth()':
            self.dm.adjustPlayerHealth(obj, state)
    
    def test_SitOn(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            self.dm.setPlayerHealth(50)
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertEqual(self.dm.getPlayerHealth(), i['target'])    



class Take(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"take armor",     "obj":"armor",     "room":"ar" },
              { "cmd":"take axe",     "obj":"axe",     "room":"tr" },
              { "cmd":"take book of locks",  "obj":"book of locks",   "room":"cl" },
              { "cmd":"take book of spells",  "obj":"book of spells",   "room":"wl" },
              { "cmd":"take bottle of gatorade",  "obj":"bottle of gatorade",   "room":"jl" },
              { "cmd":"take bottle of water",  "obj":"bottle of water",   "room":"bh" },
              { "cmd":"take bottleopener",  "obj":"bottleopener",   "room":"jl" },
              { "cmd":"take brass lantern",  "obj":"brass lantern",   "room":"sq" },
              { "cmd":"take broken lantern",  "obj":"broken lantern",   "room":"wl" },
              { "cmd":"take cloak",  "obj":"cloak",   "room":"ct" },
              { "cmd":"take earthenware",  "obj":"earthenware",   "room":"bh" },
              { "cmd":"take fine china",  "obj":"fine china",   "room":"bh" },
              { "cmd":"take gem",  "obj":"gem",   "room":"bd" },
              { "cmd":"take golden key",  "obj":"golden key",   "room":"bd" },
              { "cmd":"take green apple",  "obj":"green apple",   "room":"kt" },
              { "cmd":"take helmet",  "obj":"helmet",   "room":"ar" },
              { "cmd":"take kitchen knife",  "obj":"kitchen knife",   "room":"kt" },
              { "cmd":"take lockpick",  "obj":"lockpick",   "room":"sr" },
              { "cmd":"take machete",  "obj":"machete",   "room":"ce" },
              { "cmd":"take magical ring",  "obj":"magical ring",   "room":"tr" },
              { "cmd":"take matches",  "obj":"matches",   "room":"kt" },
              { "cmd":"take mushrooms",  "obj":"mushrooms",   "room":"sr" },
              { "cmd":"take note",  "obj":"note",   "room":"ca" },
              { "cmd":"take red apple",  "obj":"red apple",   "room":"sq" },
              { "cmd":"take sabre",  "obj":"sabre",   "room":"ar" },
              { "cmd":"take scroll",  "obj":"scroll",   "room":"jl" },
              { "cmd":"take shale rocks",  "obj":"shale rocks",   "room":"ce" },
              { "cmd":"take slate rocks",  "obj":"slate rocks",   "room":"pw" },
              { "cmd":"take stoneware",  "obj":"stoneware",   "room":"ca" },
              { "cmd":"take treasure",  "obj":"treasure",   "room":"tr" },
              { "cmd":"take warhammer",  "obj":"warhammer",   "room":"ar" } ]

    def checkDependency(self, method, obj, expect):
        if method == 'isObjectInInventory()':
            return self.dm.isObjectInInventory(obj) == expect
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect  
        if method == 'isObjectInRoom()':
            return self.dm.isObjectInRoom(obj) == expect 
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect     
        if method == 'isSpaceInInventory()':
            return self.dm.isSpaceInInventory(obj) == expect  
        if method == 'isObjectAcquirable()':
            return self.dm.isObjectAcquirable(obj) == expect 
            
    def takeAction(self, method, obj, state):
        if method == 'addInventoryObject()':
            self.dm.addInventoryObject(obj, state)
        if method == 'removeRoomObject()':
            self.dm.removeRoomObject(obj, state)
    
    def test_Take(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            self.dm.setObjectVisible(i['obj'], True)
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3,4,5]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            self.dm.setPlayerHealth(100)
            for k in [0,1]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertTrue(self.dm.isObjectInInventory(a[k]['object']))
            self.assertFalse(self.dm.isObjectInRoom(a[k]['object']))
            self.dm.removeInventoryObject(a[k]['object'])
                


class Unequip(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"unequip armor",     "obj":"armor"   },
              { "cmd":"unequip axe",     "obj":"axe"   },
              { "cmd":"unequip cloak",     "obj":"cloak"   },
              { "cmd":"unequip helmet",     "obj":"helmet"   },
              { "cmd":"unequip kitchen knife",     "obj":"kitchen knife"   },
              { "cmd":"unequip machete",     "obj":"machete"   },
              { "cmd":"unequip magical ring",     "obj":"magical ring"   },
              { "cmd":"unequip sabre",            "obj":"sabre"   },
              { "cmd":"unequip warhammer",   "obj":"warhammer"   }]

    def checkDependency(self, method, obj, expect):
        if method == 'isObjectInInventory()':
            return self.dm.isObjectInInventory(obj) == expect
        if method == 'isObjectEquipped()':
            return self.dm.isObjectEquipped(obj) == expect  
            
    def takeAction(self, method, obj, state):
        if method == 'setObjectEquipped()':
            self.dm.setObjectEquipped(obj, state)

    def test_Unequip(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.addInventoryObject(i['obj'], True)
            self.dm.setObjectEquipped(i['obj'], True)
            d = dep['commands'][index]['dependencies']
            for j in [0,1]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertFalse(self.dm.isObjectEquipped(a[k]['object']))
            self.dm.removeInventoryObject(a[k]['object'])
                

class Unlock1(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"unlock south",     "obj":"south",  "room":"ce",  "key":"golden key"   } ]

    def checkDependency(self, method, obj, expect):
        if method == 'isExitInRoom()':
            return self.dm.isExitInRoom(obj) == expect
        if method == 'isExitVisible()':
            return self.dm.isExitVisible(obj) == expect  
        if method == 'isExitUnlocked()':
            return self.dm.isExitUnlocked(obj) == expect     
        if method == 'isExitKeyInInventory()':
            return self.dm.isExitKeyInInventory(obj) == expect   
            
    def takeAction(self, method, obj, state):
        if method == 'setExitUnlocked()':
            self.dm.setExitUnlocked(obj, state)

    def test_Unlock1(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            self.dm.addInventoryObject(i['key'])
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertTrue(self.dm.isExitUnlocked(a[k]['object']))

                
class Unlock2(unittest.TestCase):
    
    dm = DataManager()
    dm.loadNewGame()
    
    data = [  { "cmd":"unlock iron trunk",    "obj":"iron trunk",  "room":"tr",  "key":"lockpick"   } ]

    def checkDependency(self, method, obj, expect):
        if method == 'isRoomLighted()':
            return self.dm.isRoomLighted(obj) == expect
        if method == 'isObjectInRoom()':
            return self.dm.isObjectInRoom(obj) == expect  
        if method == 'isObjectVisible()':
            return self.dm.isObjectVisible(obj) == expect 
        if method == 'isObjectUnlocked()':
            return self.dm.isObjectUnlocked(obj) == expect        
        if method == 'isObjectInInventory()':
            return self.dm.isObjectInInventory(obj) == expect   
            
    def takeAction(self, method, obj, state):
        if method == 'setObjectUnlocked()':
            self.dm.setObjectUnlocked(obj, state)

    def test_Unlock2(self):
        for i in self.data:
            index = getDependencyIndex(i['cmd'])
            self.dm.setPlayerLocation(i['room'])
            self.dm.setRoomLighted(i['room'], True)
            self.dm.addInventoryObject(i['key'])
            d = dep['commands'][index]['dependencies']
            for j in [0,1,2,3,4]:
                self.assertTrue(self.checkDependency(d[j]['method'], d[j]['object'], d[j]['expect']))
            a = dep['commands'][index]['actions']
            for k in [0]:
                self.takeAction(a[k]['method'], a[k]['object'], a[k]['state'])
            self.assertTrue(self.dm.isExitUnlocked(a[k]['object']))

    
    
if __name__ == '__main__':
	unittest.main()
