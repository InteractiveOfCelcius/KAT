"""
making things easier :p
"""


_DATA=['nrv','Lotous','24.03.1']
class NRV:
	def __init__(A):A._NRV_DATA={}
	def SetKey(A,keyName,value):B=keyName;A._NRV_DATA[B]=value;return A._NRV_DATA[B]
	def GetKey(A,keyName):return A._NRV_DATA[keyName]
	def DelKey(A,keyName):del A._NRV_DATA[keyName]
def package():
	def A(args):success('NRV API is loaded and ready for production use.')
	registerCommand('nrv',A)
