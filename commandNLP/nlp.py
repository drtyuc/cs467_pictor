#!usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import unittest


class nlp():
	
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
		self.__commandTuples = []


	
	'''

	Definition: this method loads the properties to an nlp object with the returns to calls 
	to the DM module methods. This method has been deprecated as the approach to NLP has changed

	'''


	def loadProperties(self, verbList, prepList, objList, vpComboList, exitList, tupleLists):

		self.__gameVerbs = verbList
		self.__prepositions = prepList
		self.__gameObjects = objList
		self.__verbPrepositionCombos = vpComboList
		self.__exits = exitList
		self.__commandTuples = tupleLists

	'''

	Definition: this method loads the command tuple property to an nlp object with a return call 
	to the DM module getObjectTuples() as the argument. 

	'''


	def setCommandTupleProperty(tupleLists):
		self.__commandTuples = tupleLists

	'''

	Definition: accessor method for the command tuples 

	''' 

	def getCommandTupleProperty(self):
		return self.__commandTuples 

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

	def printCommandTuples(self):
		for i in self.__commandTuples:
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

