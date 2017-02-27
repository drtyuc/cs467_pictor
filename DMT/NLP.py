import re
from sets import Set
from DMT.GameData import DataManager


class NLP:
    dm = DataManager()
    dm.loadNewGame()
    dep = dm.getDependencies()
    syn = dm.getSynonyms()
    synDict = {}
    command_set = Set()
    
    def __init__(self):
        command_set = self.createCommandSet()
   
    #----------------------     
    def createCommandSet(self):
        """Builds a set of unique words used in both commands 
           and synonyms"""
        for i in self.dep['commands']:
            for k in re.findall(r'(?ms)\W*(\w+)', i['tuple']):
                self.command_set.add(k)
        for i in self.syn:
            self.command_set.add(i.word)
            self.synDict[i.word] = i.map
        
        return
    
    #----------------------
    def LevenshteinDistanceRecursive(self, s, ls, t, lt):
        """Algorithm is very inefficient because it recomputes
           the Levenshtein distance of the same substrings many
           times ... unuseable for strings greater than 20 characters"""
        if s == t:
            return 0
        if ls == 0:
            return lt
        if lt == 0:
            return ls
        
        if s[ls-1] == t[lt-1]:
            cost = 0
        else: 
            cost = 1
        
        d1 = self.LevenshteinDistanceRecursive(s,   ls-1, t, lt)   + 1
        d2 = self.LevenshteinDistanceRecursive(s,   ls,   t, lt-1) + 1
        d3 = self.LevenshteinDistanceRecursive(s  , ls-1, t, lt-1) + cost
        return min(d1, d2, d3) 
        
    #----------------------    
    def LevenshteinDistanceIterative(self, s, ls, t, lt):
        """Algorighm calculates the Levenshtein distance without 
           repeating any calculations ... thus making it much more 
           efficient than the recursive algorithm"""
        if s == t:
            return 0
        if ls == 0:
            return lt
        if lt == 0:
            return ls
        
        v0 = [0] * (lt+1)
        v1 = [0] * (lt+1)
        for i in range(0, len(v0)):
            v0[i] = i
         
        for i in range(0, ls):
            v1[0] = i + 1
            for j in range(0, lt):
                if s[i] == t[j]:
                    cost = 0
                else:
                    cost = 1
                v1[j+1] = min(v1[j] + 1, v0[j+1] + 1, v0[j] + cost)
            for j in range(0, len(v0)):
                v0[j] = v1[j]
            
        return v1[lt]
   
    #----------------------      
    def getWordMatch(self, w, algorithm):
        """Map word to a supported command word or synonymn"""
        mincost = 1
        word = ""
        for i in self.command_set:
            if algorithm == "iterative":
                cost = self.LevenshteinDistanceIterative(w,len(w),i,len(i)) / float(len(w) + len(i))
            else:
                cost = self.LevenshteinDistanceRecursive(w,len(w),i,len(i)) / float(len(w) + len(i))
            if cost < mincost:
                mincost = cost
                word = i
        if (mincost <= 0.15):
            return word
        else:
            return ''

    #----------------------         
    def getCommandMatch(self, sentence, algorithm):
        """Map player's input to a supported command"""
        count = 0
        tokens = re.findall(r'(?ms)\W*(\w+)', sentence)
        sen = ""
        for i in tokens:
            count += 1
            word = self.getWordMatch(i, algorithm)
            if len(word):
                if count == len(tokens):
                    sen += word
                else:
                    sen += word + " "
        
        newsentence = self.replaceSynonyms(sen)        
        return newsentence
    
        
    #----------------------             
    def replaceSynonyms(self, sentence):
        """Replace synonyms with their supported game verb"""
        count = 0
        sen = ""
        tokens = re.findall(r'(?ms)\W*(\w+)', sentence)
        for i in tokens:
            count += 1
            word = i
            if i in self.synDict:
                word = self.synDict[i]
            if count == len(tokens):
                sen += word
            else:
                sen += word + " "
                
        return sen
                    

