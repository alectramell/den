import os
import sys
import platform
import hashlib

OSname = str(platform.system())

if OSname == "Windows":

	def clear():

		import os
		os.system('cls')

else:

	def clear():

		import os
		os.system('clear')

def md5(xvar):

	import hashlib
	yvar = hashlib.md5(xvar.encode())
	return(yvar.hexdigest())