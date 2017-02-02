import nlp 

def main():

	TESTING = True 

	#if unit testing desired, no user interaction occurs...
	if TESTING:
		gameNLP = nlp.nlp()
		gameNLP.buildSynonymDict()
		gameNLP.testBuildTuple()
		
	else:

		gameNLP.buildSynonymDict()
		commandTuple = ()
		while not any(commandTuple):
			command = raw_input("Your move: ")
			commandTuple = gameNLP.buildTuple(command)
			if not any(commandTuple):
				print "I don't understand..."
		print commandTuple
		

if __name__ == '__main__':
	main()