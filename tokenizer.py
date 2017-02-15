#!/usr/bin/env python
import re
from DMT.GameData import DataManager

class tokenizer():

    dm = DataManager()
    dm.loadNewGame()
    dep = dm.getDependencies()
    
    def findCommand(self, playerInput):
        for i in self.dep['commands']:
            playerTokens = re.findall(r'(?ms)\W*(\w+)', playerInput)
            found = True
            for k in re.findall(r'(?ms)\W*(\w+)', i['tuple']):
                if k not in playerTokens:
                    found = False
                    break
            if found:
                return i['tuple']
        return "No command found"
    

    def getPlayerInput(self):
        playerinput = ""
        while playerinput != "quit":
            playerinput = raw_input("Enter unstructure text: ")
            if playerinput == "quit":
                print "GOOD BYE!"
                return
            command = self.findCommand(playerinput)
            print "Command: " + command
        return

    
    def showMenu(self):
        choice = "" 
        while (choice != "1") and (choice != "2"):
            print
            print "1) Start tokenization"
            print "2) Exit"
            choice = str(raw_input("Enter your choice> "))
        if choice == "1":
            self.getPlayerInput()
        return


    def runit(self):
	self.showMenu()



""" MAIN """
if __name__ == "__main__":
    hd = tokenizer()
    hd.runit()
