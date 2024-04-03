"""
KAT Package library made by Interactive Of Celcius and handled by them!
"""

_KATVER = float('24.42')

def KAT(args):
    if args:
        mtod = requests.get('https://interactiveofcelcius.github.io/KAT/mtod')
        ver = requests.get('https://interactiveofcelcius.github.io/KAT/ver.txt')
        if mtod.status_code and ver.status_code == 200:
            print(Fore.CYAN + mtod.text)
            if float(ver.text) != _KATVER:
                warn(f'You are using an outdated version ({ver.text}) of KAT, please update it with "kat update kat"')
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
        if args[0] == 'update':
            package_name = args[1]
            package_url = f'https://interactiveofcelcius.github.io/KAT/{package_name}.py'
            package_file_path = os.path.join(folder_path, f"{package_name}.py")
            if os.path.exists(package_file_path):
                print(f"Updating package {package_name}...")
                os.remove(package_file_path)
            print(f"Downloading package {package_name}...")
            response = requests.get(package_url)
            if response.status_code == 200:
                succes(f"Package {package_name} found.")
                with open(package_file_path, 'w') as package_file:
                    package_file.write(response.text)
                succes(f"Package '{package_name}' downloaded and updated successfully.")
                warn('''=================WARNING===================
Please restart KATLine to get the updated packages!
===========================================
                     ''')
            else:
                warn(f"Package '{package_name}' does not exist.")
        if args[0] == 'uninstall':
            package_name = args[1]
            if package_name != 'kat':
                package_file_path = os.path.join(folder_path, f"{package_name}.py")
                if os.path.exists(package_file_path):
                    print(f"Removing package {package_name}...")
                    os.remove(package_file_path)
                    succes("Package removed. To get the commands removed please reload KATLine")
            else:
                warn("You can't uninstall KAT")

            
    else:
        print(f'KAT is a command used to install packages for KATLine.')


def doQuit(args):
    exit()
    

    
    
# Register all the commands
registerCommand('kat', KAT)
registerCommand('quit', doQuit)
