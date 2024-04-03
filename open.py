"""
open is a useful command to open the current path folder.
"""

_DATA = ["open", "psvks"]


def package():
    def Open(args):
        print(_DATA)
        try:
            print(currentPath)
            os.system(f'explorer.exe {currentPath}')
            print('Opening to the current path')
        except Exception as e:
            warn(f'open command error: {e}')
        
        
    registerCommand('open', Open)
