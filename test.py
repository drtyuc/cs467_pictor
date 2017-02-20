#!/usr/bin/env python
###############################################
from DMT.GameData import DataManager
#from DMT.nlp import nlp
from commandNLP.nlp import nlp


class Test():
    
    dm = DataManager()
    dm.loadNewGame()
    dep = dm.getDependencies()
    
    
    andrew = nlp()
    andrew.loadProperties(dm.getVerbs(), 
                          dm.getPrepositions(),
                          dm.getObjects(), 
                          dm.getVerbPrepositionCombos(),
                          dm.getExits(),
                          dm.getCommandTuples())
                          
                          
            
    def showProperties(self):
        self.andrew.printVerbs()
        self.andrew.printPrepositions()
        self.andrew.printObjects()
        self.andrew.printVerbPrepositionCombos()
        self.andrew.printExits()
        print "COMMAND TUPLES"
        print self.andrew.printCommandTuples()
        print "COMMAND TUPLES LIST"
        print self.andrew.getCommandTupleProperty()
 

    def runit(self):
	self.showProperties()
 

if __name__ == "__main__":
    test = Test()
    test.runit()
