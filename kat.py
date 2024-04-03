"""
KAT Package library made by Interactive Of Celcius and handled by them!
"""

def katCommandExecute(args):
    if args:
        mtod = requests.get('https://interactiveofcelcius.github.io/KAT/mtod')
        if mtod.status_code == 200:
            print(Fore.CYAN + mtod.text)
        else:
            warn("MTOD Couldn't be loaded. Please verify if the server is on!")
        if args[0] == 'install':
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
                print(f"Folder '.packages' created successfully.")
            else:
                print(f"Folder '.packages' already exists.")
            print(f'Finding package {args[1]}...')
            r = requests.get(f'https://interactiveofcelcius.github.io/KAT/{args[1]}.py')
            if r.status_code == 200:
                print('Package found.')
                package_file_path = os.path.join(folder_path, f"{args[1]}.py")
                with open(package_file_path, 'w') as package_file:
                    package_file.write(r.text)
                    exec(r.text)
                succes(f"Package '{args[1]}' downloaded and ready to use.")
            else:
                warn(f'package: {args[1]} does not exist.')
    else:
        print(f'KAT is a command used to install packages for KATLine.')


def doQuit(args):
    exit()
    

    
    
# Register all the commands
registerCommand('kat', katCommandExecute)
registerCommand('quit', doQuit)
