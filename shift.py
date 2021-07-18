import os
import sys
import time
import string
from threading import Thread

def shift(xvar, yvar):

	xnum = int(xvar)
	xstr = str(yvar.lower())

	ALPHA = list(string.ascii_lowercase[0:26])
	SHIFT = list(string.ascii_lowercase[xnum:26]+string.ascii_lowercase[0:xnum])
	
	xmid = xstr.replace(ALPHA[0], '.00').replace(ALPHA[1], '.01').replace(ALPHA[2], '.02').replace(ALPHA[3], '.03').replace(ALPHA[4], '.04').replace(ALPHA[5], '.05').replace(ALPHA[6], '.06').replace(ALPHA[7], '.07').replace(ALPHA[8], '.08').replace(ALPHA[9], '.09').replace(ALPHA[10], '.10').replace(ALPHA[11], '.11').replace(ALPHA[12], '.12').replace(ALPHA[13], '.13').replace(ALPHA[14], '.14').replace(ALPHA[15], '.15').replace(ALPHA[16], '.16').replace(ALPHA[17], '.17').replace(ALPHA[18], '.18').replace(ALPHA[19], '.19').replace(ALPHA[20], '.20').replace(ALPHA[21], '.21').replace(ALPHA[22], '.22').replace(ALPHA[23], '.23').replace(ALPHA[24], '.24').replace(ALPHA[25], '.25')
	xout = xmid.replace('.00', SHIFT[0]).replace('.01', SHIFT[1]).replace('.02', SHIFT[2]).replace('.03', SHIFT[3]).replace('.04', SHIFT[4]).replace('.05', SHIFT[5]).replace('.06', SHIFT[6]).replace('.07', SHIFT[7]).replace('.08', SHIFT[8]).replace('.09', SHIFT[9]).replace('.10', SHIFT[10]).replace('.11', SHIFT[11]).replace('.12', SHIFT[12]).replace('.13', SHIFT[13]).replace('.14', SHIFT[14]).replace('.15', SHIFT[15]).replace('.16', SHIFT[16]).replace('.17', SHIFT[17]).replace('.18', SHIFT[18]).replace('.19', SHIFT[19]).replace('.20', SHIFT[20]).replace('.21', SHIFT[21]).replace('.22', SHIFT[22]).replace('.23', SHIFT[23]).replace('.24', SHIFT[24]).replace('.25', SHIFT[25])

	return(xout)

def unshift(xvar, yvar):

	xnum = int(xvar)
	xstr = str(yvar.lower())

	ALPHA = list(string.ascii_lowercase[0:26])
	SHIFT = list(string.ascii_lowercase[xnum:26]+string.ascii_lowercase[0:xnum])
	
	xmid = xstr.replace(SHIFT[0], '.00').replace(SHIFT[1], '.01').replace(SHIFT[2], '.02').replace(SHIFT[3], '.03').replace(SHIFT[4], '.04').replace(SHIFT[5], '.05').replace(SHIFT[6], '.06').replace(SHIFT[7], '.07').replace(SHIFT[8], '.08').replace(SHIFT[9], '.09').replace(SHIFT[10], '.10').replace(SHIFT[11], '.11').replace(SHIFT[12], '.12').replace(SHIFT[13], '.13').replace(SHIFT[14], '.14').replace(SHIFT[15], '.15').replace(SHIFT[16], '.16').replace(SHIFT[17], '.17').replace(SHIFT[18], '.18').replace(SHIFT[19], '.19').replace(SHIFT[20], '.20').replace(SHIFT[21], '.21').replace(SHIFT[22], '.22').replace(SHIFT[23], '.23').replace(SHIFT[24], '.24').replace(SHIFT[25], '.25')
	xout = xmid.replace('.00', ALPHA[0]).replace('.01', ALPHA[1]).replace('.02', ALPHA[2]).replace('.03', ALPHA[3]).replace('.04', ALPHA[4]).replace('.05', ALPHA[5]).replace('.06', ALPHA[6]).replace('.07', ALPHA[7]).replace('.08', ALPHA[8]).replace('.09', ALPHA[9]).replace('.10', ALPHA[10]).replace('.11', ALPHA[11]).replace('.12', ALPHA[12]).replace('.13', ALPHA[13]).replace('.14', ALPHA[14]).replace('.15', ALPHA[15]).replace('.16', ALPHA[16]).replace('.17', ALPHA[17]).replace('.18', ALPHA[18]).replace('.19', ALPHA[19]).replace('.20', ALPHA[20]).replace('.21', ALPHA[21]).replace('.22', ALPHA[22]).replace('.23', ALPHA[23]).replace('.24', ALPHA[24]).replace('.25', ALPHA[25])

	return(xout)

# Usage..
#
#	>>> from shift import *
#	>>> 
#	>>> shift(5, 'hello world')
#	>>> 'mjqqt btwqi'
#	>>>
#	>>> unshift(5, 'mjqqt btwqi')
#	>>> 'hello world'