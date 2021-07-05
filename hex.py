import os
import sys
import platform
import binascii

OSname = str(platform.system())

if OSname == "Windows":

	def clear():

		import os
		os.system('cls')

else:
	def clear():

		import os
		os.system('clear')

def hex(xvar):

	import binascii
	yvar = bytes(xvar, encoding='utf-8')
	zvar = str(binascii.hexlify(yvar))
	avar = zvar.replace("b","")
	ovar = avar.replace("'","")
	return(ovar)

def unhex(xvar):

	import binascii
	yvar = str(xvar)
	zvar = str(binascii.unhexlify(yvar))
	avar = zvar.replace("b","")
	ovar = avar.replace("'","")
	return(ovar)
