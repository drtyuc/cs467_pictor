#!usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import unittest
import difflib #we should be able to use this...


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
	to the DM module getCommandTuples() as the argument. 

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

		#synonymFilePath = '/Users/andrewbagwell/Desktop/capstone/cs467_pictor/data/synonymFile.txt'
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

	Definition: Fuzzy matches two words and returns a score based on that match

	

	'''

	def doFuzzyMatchNaive(self, inputPart, tuplePart):

		#simple attempt to fuzzy match words
		sm = difflib.SequenceMatcher(None, inputPart, tuplePart)
		straightFuzzMatchRatio = sm.ratio()

		#debugging
		#print "FUZZ MATCH RATIO for "  + inputPart + "&" + tuplePart + "- " + str(straightFuzzMatchRatio)

		if straightFuzzMatchRatio > .62: # kind of arbitrary, but this should handle some issues where there is only a low fuzzy match a tuple (e.g, light room being matched to drop mushrooms) 
			return straightFuzzMatchRatio
		else:
			return 0

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
	Definition: This function takes the user input and returns the tuple that it matched to. 
	This is similar to the older method buildTuple() but supports or token oriented approach to NLP. This method iterates through 
	each supported tuple and attempts to match 

	'''

	
	def matchTuple(self, commandString):

		commandTokens = self.parseCommand(commandString)

		highScore = 0
		currentScore = 0
		tupleList = self.getCommandTupleProperty()

		tupleReturned = ()

		for commandTuple in tupleList:
			#parse the tuple itself into token
			tupleParts = commandTuple.split()
			currentScore = 0

			#iterate through tokens produced by user input
			for tupPart in tupleParts:
				
				for word in commandTokens:

					if word == tupPart:
						currentScore += 1
				
					elif word in self.__synonymsDictionary:
						dictVal = self.__synonymsDictionary[word]
						if dictVal == tupPart:
							currentScore += 1									
					else:
						currentScore += self.doFuzzyMatchNaive(word, tupPart)
			
			if currentScore > highScore:
					
				highScore = currentScore
				tupleReturned = commandTuple

				'''
				#check to see if the length of the tuple is greater than the length of the input tokenlist
				#this should control against look at/look at altar problem but creates problem with "light room" and (light brass lanterm)

				if len(tupleParts) > len(commandTokens):
					continue 
				else:
					highScore = currentScore
					tupleReturned = commandTuple
				'''

		#DEBUGGING HERE - This comes out in production version
		print "highest score = " + str(highScore)
		print "matched tuple = " + str(tupleReturned)

		return tupleReturned


	'''

	Definition: takes the command string entered by the user. It then tokenizes that input. Next, it performs
	the processes that input. THIS METHOD IS DEPRECATED AND WILL BE DELETED
	
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

	def testMatchTuple(self):
		assert(self.matchTuple(['drink', 'bottle'])==('drink bottle'))
		assert(self.matchTuple(['drop', 'with', 'armor'])==())
		assert(self.matchTuple(['drop', 'matches'])==('drop matches'))
		assert(self.matchTuple(['eat', 'mushrooms'])==('eat mushrooms'))


		print "Tests passed!"

if __name__ == '__main__':
	nlp()

