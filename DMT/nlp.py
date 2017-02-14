#!usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import unittest

class nlp():
    
    def __init__(self):
        self.__gameVerbs = []
        self.__prepositions = []
        self.__gameObjects = []
        self.__verbPrepositionCombos = {}
        self.__exits = []
        

    def loadProperties(self, A, B, C, D, E):
        self.__gameVerbs = A
        self.__prepositions = B
        self.__gameObjects = C
        self.__verbPrepositionCombos = D
        self.__exits = E
        
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
