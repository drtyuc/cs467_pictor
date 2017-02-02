#!usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import unittest

TESTING = True

cwd = os.getcwd()

gameVerbs = ["drink", "drop", "eat", "help", "hit", "inventory", "loadgame", "look", "pull", "push",
"savegame", "take", "use", "wear", "wield"]

prepositions = ["above", "at", "behind", "into", "on", "under", "with" ]

gameObjects = [ "altar", "apple", "armor", "axe", "bearskin", "bed", "book", "books", "bones", "bottle", "chair", "chairs",
                 "chandelier", "cloak", "desk", "dinnerware", "gem", "hearth", "helmet", "key", "key-rung", "knife",
                 "lantern", "lever", "lockpick", "matches", "mattress", "mushrooms", "nightstand", "note",
	  			"painting", "paintings", "ring", "rocks", "rug", "runes", "safe", "scroll", "shelf", "shelves", "sign", "stool",
                 "stools", "sword", "table", "tables", "tapestries", "tools", "treasure", "tree", "trunk", "warhammer"]


verbPrepositionCombos = {'look':['at', 'under', 'above', 'into', 'behind'], 'take': [], 
						'help': ['with'], 'inventory': [], 'use': ['on', 'with'], 'drop' : ['at', 'behind', 'into', 'on'], 'eat': [],
						'drink':[], 'pull': [], 'hit': [], 'put': [], 'hit': [], 'put': ['on', 'into', 'under', 'above', 'with'],
						'push': ['on'], 'wield': [], 'wear': [],}
synonymsDictionary = {}




'''

Definition: builds the dictionary used to check if a command issued is synonymous with 

'''

def buildSynonymDict():

	
	synonymFilePath = cwd + "/synonymFile.txt" #file source: https://justenglish.me/2014/04/18/synonyms-for-the-96-most-commonly-used-words-in-english/
	

	with open(synonymFilePath, 'r') as f:
		for line in f:
			splitLine = line.split('-')
			verb, synonymList = splitLine
			verb = verb.lower()
			verb = verb.strip(' \t\n\r')
			parsedSynonyms = synonymList.split(",")
			for word in parsedSynonyms:
				word = word.strip(' \t\n\r')
				synonymsDictionary[word] = verb

'''

Definition: parses command passed by user into tokens 

Post Conditions: Returns 

'''


def parseCommand(commandString):

	commandString = commandString.lower()
	commandString = commandString.split()
	for word in commandString:
		word = word.strip('.,!;')

	return commandString


'''

Definition: takes the command string entered by the user. It then tokenizes that input. Next, it performs
the processes that input: 

'''


def buildTuple(commandString):

	tupleReturned = ()


	#get tokens
	parsedCommand = parseCommand(commandString)

	#get the verb, check to see if it exists in the dict, if it doesn't, return empty tuple, 
	verbCommand = parsedCommand[0] 
	if verbCommand in synonymsDictionary:
		verbCommand = synonymsDictionary[verbCommand]
	else:
		return tupleReturned

	#get the preposition, check to see if it exists in the dictionary, if so, check to see if pair with verb is valid

	if len(parsedCommand) == 2:
		prepositionCommand = None
		permittedPreps = verbPrepositionCombos[verbCommand]
		if any(permittedPreps):
			return tupleReturned 

	else:
		prepositionCommand = parsedCommand[1]
		if prepositionCommand in synonymsDictionary:
			prepositionCommand = synonymsDictionary[prepositionCommand]
			#if verb in verbPrepositionCombos:
			permittedPreps = verbPrepositionCombos[verbCommand]
			if prepositionCommand not in permittedPreps:
				return tupleReturned 
		else:
			return tupleReturned

	#get the object 

	if len(parsedCommand) == 2:
		objectCommand = parsedCommand[1]
	else:
		objectCommand = parsedCommand[2]
	
	if objectCommand not in gameObjects:
		return tupleReturned

	#build the actual tuple and return it

	tupleReturned = (verbCommand, prepositionCommand, objectCommand)
	return tupleReturned


'''
Class used for unit Testing 

'''

def testBuildTuple(self):
		assert(buildTuple("drink bottle")==('drink', None, 'bottle'))
		assert (buildTuple("drop with armor")==())
		assert (buildTuple("drop at bed")==('drop', 'at', 'bed'))
		assert (buildTuple("eat under book")==())
		assert(buildTuple("eat apple")==('eat', None, 'apple'))
		assert(buildTuple("help hit bearskin")==())
		assert(buildTuple("help with bones")==('help', 'with', 'bones'))


def main():

	#if unit testing desired, no user interaction occurs...
	if TESTING:
		buildSynonymDict()
		testBuildTuple()
		
	else:

		buildSynonymDict()
		commandTuple = ()
		while not any(commandTuple):
			command = raw_input("Your move: ")
			commandTuple = buildTuple(command)
			if not any(commandTuple):
				print "I don't understand..."
		print commandTuple
		
	

if __name__ == '__main__':
	if TESTING:
		unittest.main()
	else:
		main()