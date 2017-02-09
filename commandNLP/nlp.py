#!usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import unittest


class nlp():
	"""I have the values for the properties already loaded here. See below function for the likely
	future state of the constructor """
	def __init__(self):
		
		self.__cwd = os.getcwd()

		self.__gameVerbs = ["drink", "drop", "eat", "equip", "go", "help", "hit", "inventory", "loadgame", "look", "pull", "push",
						  "savegame", "take", "use", "wear", "wield"]

		self.__prepositions = ["above", "at", "behind", "into", "on", "under", "with" ]

		self.__gameObjects = [ "altar", "apple", "armor", "axe", "bearskin", "bed", "book", "books", "bones", "bottle", "chair", "chairs",
                 			"chandelier", "cloak", "desk", "dinnerware", "gem", "hearth", "helmet", "key", "key-rung", "knife",
                 			"lantern", "lever", "lockpick", "matches", "mattress", "mushrooms", "nightstand", "note",
	  						"painting", "paintings", "ring", "rocks", "rug", "runes", "safe", "scroll", "shelf", "shelves", "sign", "stool",
                 			"stools", "sword", "table", "tables", "tapestries", "tools", "treasure", "tree", "trunk", "warhammer"]
		self.__verbPrepositionCombos = {'look':['at', 'under', 'above', 'into', 'behind'], 'take': [], 
							'help': ['with'], 'inventory': [], 'use': ['on', 'with'], 'drop' : ['at', 'behind', 'into', 'on'], 'eat': [],
							'drink':[], 'pull': [], 'hit': [], 'put': [], 'put': ['on', 'into', 'under', 'above', 'with'],
							'push': ['on'], 'wield': [], 'wear': [], 'go':[]}
		self.__synonymsDictionary = {}

	
	'''

	Definition: this function sets the properties that will be used by the nlp object to potentially match
	strings. It will likely take the string returned by the call to dm.getObjectList(). I may move this
	into the constructor but for right now it easier for testing purposes to do it with this function

	'''


	def loadProperties(verbList, prepList, objList, vpComboList):

		self.__gameVerbs = verbList
		self.__prepositions = prepList
		self.__gameObjects = objList
		self.__verbPrepositionCombos = vpComboList



	'''

	Definition: builds the dictionary used to check if a command issued is synonymous with a supported game word (verbs/prepositions)

	'''

	def buildSynonymDict(self):

		synonymFilePath = self.cwd + "/synonymFile.txt" #file source: https://justenglish.me/2014/04/18/synonyms-for-the-96-most-commonly-used-words-in-english/
		with open(synonymFilePath, 'r') as f:
			for line in f:
				splitLine = line.split('-')
				verb, synonymList = splitLine
				verb = verb.lower()
				verb = verb.strip(' \t\n\r')
				parsedSynonyms = synonymList.split(",")
				for word in parsedSynonyms:
					word = word.strip(' \t\n\r')
					self.synonymsDictionary[word] = verb

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

		#get tokens
		parsedCommand = self.parseCommand(commandString)

		#get the verb, check to see if it exists in the dict, if it doesn't, return empty tuple, 
		verbCommand = parsedCommand[0] 
		if verbCommand in self.synonymsDictionary:
			verbCommand = self.synonymsDictionary[verbCommand]
		else:
			return tupleReturned

	#get the preposition, check to see if it exists in the dictionary, if so, check to see if pair with verb is valid

		if len(parsedCommand) == 2:
			prepositionCommand = None
			permittedPreps = self.verbPrepositionCombos[verbCommand]
			if any(permittedPreps):
				return tupleReturned 

		else:
			prepositionCommand = parsedCommand[1]
			if prepositionCommand in self.synonymsDictionary:
				prepositionCommand = self.synonymsDictionary[prepositionCommand]
				permittedPreps = self.verbPrepositionCombos[verbCommand]
				if prepositionCommand not in permittedPreps:
					return tupleReturned 
			else:
				return tupleReturned

		#get the object 

		if len(parsedCommand) == 2:
			objectCommand = parsedCommand[1]
		else:
			objectCommand = parsedCommand[2]
	
		if objectCommand not in self.gameObjects:
			return tupleReturned

		#build the actual tuple and return it

		tupleReturned = (verbCommand, prepositionCommand, objectCommand)
		return tupleReturned


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

