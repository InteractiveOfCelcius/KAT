
"""
Execute python code inside the KATLine Enviroment
"""
_DATA = ["package.executor.net", 'KAT Indrustries', "24.03.1"]

def package():
	def execute(args):
		if args:
			pynormite = ' '.join(args)
			exec(pynormite)

		else:
			warn('You need to specify a python instruction')

	registerCommand('exec', execute)
