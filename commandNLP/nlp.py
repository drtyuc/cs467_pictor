#!usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import unittest


class nlp():
	
	'''

	Definition: this is the old constructor with hard coded values used. We can use this for midway test.
	Hopefully, we wll get this sorted out!

	
	def __init__(self):
		

		self.__gameVerbs = ["drink", "drop", "east", "eat", "equip", "go", "help", "hit", "inventory", "lay", "light", "loadgame", "look", "north", 
							"pull", "push", "read", "savegame", "sit", "south", "take", "unequip", "unlock", "use", "wear", "west", "wield"]

		self.__prepositions = ["above", "at", "behind", "into", "on", "under", "with" ]

		self.__gameObjects = [ "altar", "apple", "armor", "axe", "bat skeleton", "bearskin", "bed","bell archway", "book", "books", "bones", "bottle", "cat skeleton", "chair", "chairs",
							"chandelier", "cloak", "corrugated steel door", "creaking cell door", "desk", "dinnerware", "east", "gem", "hearth", "helmet", "human skeleton" "key", "key-rung", "knife",
							"lantern", "lever", "lockpick", "long dark tunnel", "matches", "mattress", "mushrooms", "monstrous archway", "nightstand", "north", "note", "oblivion gate", "old wooden door",
							"painting", "paintings", "ring", "rocks", "rolling shutter door", "rug", "runes", "rusted spiral staircase", "rusting iron door", "safe", "scroll", "shelf", "shelves", "sign", 
							"smoky glazed doors", "solid metal door", "splintered double doors", "south", "stool", "stools", "swinging door", "sword", "table", "tables", "tapestries", "tools", "treasure", "tree", "trunk", "warhammer", "west", "winder stairs"]

		self.__verbPrepositionCombos = {'drink':[], 'drop' : ['at', 'behind', 'into', 'on'], 'eat': [], 'equip': [], 'go':[], 
										'help': ['with'], 'hit': [], 'inventory': [], 'lay' : ['on'], 'light': [],  'look':['at', 'under', 'above', 'into', 'behind'], 
										'pull': [],  'put': ['on', 'into', 'under', 'above', 'with'], 'push': ['on'], 'read' : [], 
										'sit': ['on'], 'take': [], 'unequip': [], 'unlock': [], 'use': ['on', 'with'], 'wear': [], 'wield': []}
		
		self.__synonymsDictionary = {}


	'''

	'''
	
	Description: constructor for NLP objects

	'''

	def __init__(self):
		
		self.__cwd = os.getcwd()
		self.__gameVerbs = []
		self.__prepositions = []
		self.__gameObjects = []
		self.__verbPrepositionCombos = {}
		self.__synonymsDictionary = {}
		self.__exits = []


	
	'''

	Definition: this method loads the properties to an nlp object with the returns to calls 
	to the DM module methods

	'''


	def loadProperties(self, verbList, prepList, objList, vpComboList):

		self.__gameVerbs = verbList
		self.__prepositions = prepList
		self.__gameObjects = objList
		self.__verbPrepositionCombos = vpComboList



	'''

	Definition: builds the dictionary used to check if a command issued is synonymous with a supported game word (verbs/prepositions)

	'''

	def buildSynonymDict(self):

		synonymFilePath = self.__cwd + "/data/synonymFile.txt" #file source: https://justenglish.me/2014/04/18/synonyms-for-the-96-most-commonly-used-words-in-english/
		with open(synonymFilePath, 'r') as f:
			for line in f:
				splitLine = line.split('-')
				verb, synonymList = splitLine
				verb = verb.lower()
				verb = verb.strip(' \t\n\r')
				parsedSynonyms = synonymList.split(",")
				for word in parsedSynonyms:
					word = word.strip(' \t\n\r')
					self.__synonymsDictionary[word] = verb

	'''

	Definition: parses command passed by user into tokens 

	Post Conditions: Returns a list of token strings

	'''

	def parseCommand(self, commandString):

		commandString = commandString.lower()
		commandString = commandString.split()
		for word in commandString:
			word = word.strip('.,!;')
		return commandString


	'''

	Definition: takes the command string entered by the user. It then tokenizes that input. Next, it performs
	the processes that input: 
	
	'''
	def buildTuple(self, commandString):

		tupleReturned = ()

		#get tokens - parsedCommand should contain a list of at most 3 items in these formats: (verb, prep, object), (verb, object), (object)
		parsedCommand = self.parseCommand(commandString)

		if len(parsedCommand) > 1:
			
			#get the verb, check to see if it exists in the dict, if it doesn't, return empty tuple, 
			verbCommand = parsedCommand[0] 
			if verbCommand in self.__synonymsDictionary:
				verbCommand = self.__synonymsDictionary[verbCommand]
			else:
				return tupleReturned

		#get the preposition, check to see if it exists in the dictionary, if so, check to see if pair with verb is valid

			if len(parsedCommand) == 2:
				prepositionCommand = None
				permittedPreps = self.__verbPrepositionCombos[verbCommand]
				if any(permittedPreps):
					return tupleReturned 

			else:
				prepositionCommand = parsedCommand[1]
				if prepositionCommand in self.__synonymsDictionary:
					prepositionCommand = self.__synonymsDictionary[prepositionCommand]
					permittedPreps = self.__verbPrepositionCombos[verbCommand]
					if prepositionCommand not in permittedPreps:
						return tupleReturned 
				else:
					return tupleReturned

			#get the object 

			if len(parsedCommand) == 2:
				objectCommand = parsedCommand[1]
			else:
				objectCommand = parsedCommand[2]
	
			if objectCommand not in self.__gameObjects and objectCommand not in self.__exits:
				return tupleReturned
		
		#occurs when only an "object/direct object is enter by the user "	
		elif len(parsedCommand) == 1:
			
			verbCommand = None
			prepositionCommand = None
			objectCommand = parsedCommand[0]

			if objectCommand not in self.__gameObjects and objectCommand not in self.__exits:
				return tupleReturned
		
		#when nothing is received
		else:
			return tupleReturned

		#build the actual tuple and return it
		tupleReturned = (verbCommand, prepositionCommand, objectCommand)
		return tupleReturned



	'''
	Definition: getter methods for instance properties
	'''

	def printVerbs(self):
		for i in self.__gameVerbs:
			print i
		print ""
	
	def printPrepositions(self):
		for i in self.__prepositions:
			print i
		print ""
			
	def printObjects(self):
		for i in self.__gameObjects:
			print i
		print ""
	
	def printVerbPrepositionCombos(self):
		print self.__verbPrepositionCombos
		print ""
			
	def printExits(self):
		for i in self.__exits:
			print i
		print ""


	'''
	Definition: Function used for unit Testing 

	'''

	def testBuildTuple(self):
		assert(self.buildTuple("drink bottle")==('drink', None, 'bottle'))
		assert(self.buildTuple("drop with armor")==())
		assert(self.buildTuple("drop at bed")==('drop', 'at', 'bed'))
		assert(self.buildTuple("eat under book")==())
		assert(self.buildTuple("eat apple")==('eat', None, 'apple'))
		assert(self.buildTuple("help hit bearskin")==())
		assert(self.buildTuple("help with bones")==('help', 'with', 'bones'))
		print "Tests passed!"

if __name__ == '__main__':
	nlp()

