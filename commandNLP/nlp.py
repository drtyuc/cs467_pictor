#!usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import unittest
import difflib #we should be able to use this...
import timeit


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
		self.__commands = []


	
	'''

	Description: this method loads the properties to an nlp object with the returns to calls 
	to the DM module methods. This method has been deprecated as the approach to NLP has changed

	'''


	def loadProperties(self, verbList, prepList, objList, vpComboList, exitList, tupleLists):

		self.__gameVerbs = verbList
		self.__prepositions = prepList
		self.__gameObjects = objList
		self.__verbPrepositionCombos = vpComboList
		self.__exits = exitList
		#self.__commandTuples = tupleLists
		self.__commands = []


		catchers = ['drink bottle', 'lay on', 'look at', 'look behind', 
		'look inside', 'look on', 'look under', 'sit on', 'take book']

		tupleLists.extend(self.getVerbs())
		tupleLists.extend(catchers)

		sortedTupleLists = sorted(tupleLists)

		self.__commandTuples = sortedTupleLists




	'''

	Description: accessor method for the command tuples 

	''' 

	def getCommandTupleProperty(self):
		return self.__commandTuples 

	'''

	Description: builds the dictionary used to check if a command issued is synonymous with a supported game word (verbs/prepositions)

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

	Description: This function compares two words by using python's difflib module. It calls difflib's sequence matcher
	constructor on with the two words as arguments, then calls it's ratio function. The funcitonality of difflib
	relies on a modification/tweeking of the Ratcliff Obershelp algorithm for pattern recognition

	'''

	def doRatOberNative(self, inputPart, tuplePart):

		#simple attempt to fuzzy match words
		sm = difflib.SequenceMatcher(None, inputPart, tuplePart)
		matchRatio = sm.ratio()

		#if the word isn't a 75% match, return a score of 0
		if matchRatio > .75: # kind of arbitrary, but this should handle some issues where there is only a low fuzzy match a tuple (e.g, light room being matched to drop mushrooms) 
			return matchRatio
		else:
			return 0

	'''

	Description: This function compares two words using the Levenshtein Distance Algorithm. This function
	is called within the matchTuple function below. 

	'''

	def doLevDist(self, inputPart, tuplePart):

		#since there is currently no synonym matching for this function, we have to set the threshold low
		minRatio = .70

		#get length
		inputTokenLength = len(inputPart)

		#get the length of the tuple
		tupLength = len(tuplePart)

		#build table for dynamic programming
		dpTable = [[0 for x in range(inputTokenLength +1)] for y in range(tupLength+1)]
		#fill in the first position
		dpTable[0][0] = 0
		#fill in table's top row 
		for val in range(1, inputTokenLength+1):
			dpTable[0][val] = val
		#fill in table's first column
		for val in range(1, tupLength+1):
			dpTable[val][0] = val

		#compute table
		for row in range(1, tupLength+1):

			for column in range(1, inputTokenLength+1):

				if tuplePart[row-1] == inputPart[column-1]:
					dpTable[row][column] = dpTable[row-1][column-1]
				else:
					neighbors = [(dpTable[row-1][column]), (dpTable[row][column-1]), (dpTable[row-1][column-1])]
					dpTable[row][column] = min(neighbors)+1

		#get levenshtein distance
		ld = dpTable[tupLength][inputTokenLength]
		maxLength = max([inputTokenLength, tupLength])
		matchRatio = 1- ld/(maxLength * 1.0)
		#print matchRatio

		#if the word isn't a 75% match, return a score of 0
		if matchRatio > minRatio: # kind of arbitrary, but this should handle some issues where there is only a low fuzzy match a tuple (e.g, light room being matched to drop mushrooms) 
			return matchRatio
		else:
			return 0

	

	'''

	Description: parses command passed by user into tokens 


	'''

	def parseCommand(self, commandString):

		commandString = commandString.lower()
		commandString = commandString.split()
		for word in commandString:
			word = word.strip('.,!;')
		return commandString


	'''
	
	Decription: cleans command tokens by fuzzy matching words

	'''

	def cleanCommands(self, commandList):

		cleanCommandList = []
		wordList = self.__synonymsDictionary
		threshold = .75
	
		for token in commandList:
			
			highScore = 0
			
			for word in wordList:
				currentScore = self.doLevDist(token, word)
				
				if currentScore > highScore:
					highScore = currentScore
					replacement = word
			
			if highScore < threshold:
				replacement = token
			
			cleanCommandList.append(replacement)

		print "DEBUGGING CLEANED COMMAND List " + str(cleanCommandList)
		return cleanCommandList

	'''
	Description: This function takes the user input and returns the tuple that it matched to. 
	This is similar to the older method buildTuple() but supports or token oriented approach to NLP. This method iterates through 
	each supported tuple and attempts to match 

	'''

	def matchTuple(self, commandString):


		#tokenize user input
		commandTokens = self.parseCommand(commandString)

		#clean the tokens
		cleanTokens = self.cleanCommands(commandTokens)

		#get list of supported tuples
		tupleList = self.getCommandTupleProperty()

		#variables for looping
		highScore = 0
		currentScore = 0
		tupleReturned = ()

		for commandTuple in tupleList:
			#parse the tuple itself into token
			tupleParts = commandTuple.split()
			currentScore = 0

			#iterate through tokens produced by user input
			for tupPart in tupleParts:
				
				for word in cleanTokens:

					if word == tupPart:
						currentScore += 1
				
					elif word in self.__synonymsDictionary:
						dictVal = self.__synonymsDictionary[word]
						if dictVal == tupPart:
							currentScore += 1							
					else:
						#currentScore += self.doRatOberNative(word, tupPart)
						currentScore += self.doLevDist(word, tupPart)
					

			if currentScore > highScore:
				highScore = currentScore
				tupleReturned = commandTuple

		#DEBUGGING HERE - This comes out in production version
		print "matchTuple METHOD"
		print "highest score = " + str(highScore)
		print "matched tuple = " + str(tupleReturned)

		return tupleReturned


	'''
	Description: getter methods for instance properties
	'''

	def getVerbs(self):
		return self.__gameVerbs

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
	Description: Function used for unit Testing 

	'''

	def testMatchTuple(self):
		assert(self.matchTuple(['drink', 'bottle'])==('drink bottle'))
		assert(self.matchTuple(['drop', 'with', 'armor'])==())
		assert(self.matchTuple(['drop', 'matches'])==('drop matches'))
		assert(self.matchTuple(['eat', 'mushrooms'])==('eat mushrooms'))


		print "Tests passed!"

if __name__ == '__main__':
	nlp()

