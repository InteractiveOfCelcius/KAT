
"""
Made by PSVKS. This code only works on KATLine.
Last update: 05/04/2024
"""


_DATA = ["LoadCodeAPI", "psvks", "24.03.1"]


class LoadCode:
  def __init__(self) -> None:
    pass

  def Load(self, url):
    r = requests.get(url)
    if r.status_code == 200:
      try:
        exec(r.text)
      except Exception as e:
        warn(f'LoadCode API Error: {e}')


def package():
  def LoadCodeAPI_Verify(args):
    success('LoadCode API is loaded! Made by PSVKS')
  
  
  registerCommand('loadcode', LoadCodeAPI_Verify)
