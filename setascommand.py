
_DATA = ["example", "me"]
_GLOBAL_VARS = NRV()

def ExecuteCommand(COMMAND, args):
	if lower_word(COMMAND) in commands:
		commands[lower_word(COMMAND)](args)


def package():
	if isPackageInstalled('nrv') != True:
		warn('example package error: Please install NRV API.')
	else:
		def set(args):
			if args:
				try:
					_GLOBAL_VARS.SetKey(args[0], args[1])
				except Exception as e:
					warn(f'constWarn: Please verify the command structure, exception: {e}')
			else:
				print('Missing arguments, set <variable> <value>')
		def get(args):
			if args:
				try:
					_D_VALUE_RETURN = _GLOBAL_VARS.GetKey(args[0])
					print(_D_VALUE_RETURN)
				except Exception as e:
					warn(f'constWarn: Please verify the command structure, exception: {e}')
			else:
				print('Missing arguments, get <variable>')

		
		registerCommand('set', set)
		registerCommand('get', get)
