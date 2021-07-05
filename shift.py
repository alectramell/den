import os
import sys
import platform

OSname = str(platform.system())

if OSname == "Windows":

	def clear():

		import os
		os.system('cls')
else:

	def clear():

		import os
		os.system('clear')

def shift(XVAR):

	word = str(XVAR.lower())

	XMARKS = list(['.00','.01','.02','.03','.04','.05','.06','.07','.08','.09','.10','.11','.12','.13','.14','.15','.16','.17','.18','.19','.20','.21','.22','.23','.24','.25'])

	XALPHA = list(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

	XSHIFT = list(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'])

	XTRANS = str(word.replace(XALPHA[0], XMARKS[0]).replace(XALPHA[1], XMARKS[1]).replace(XALPHA[2], XMARKS[2]).replace(XALPHA[3], XMARKS[3]).replace(XALPHA[4], XMARKS[4]).replace(XALPHA[5], XMARKS[5]).replace(XALPHA[6], XMARKS[6]).replace(XALPHA[7], XMARKS[7]).replace(XALPHA[8], XMARKS[8]).replace(XALPHA[9], XMARKS[9]).replace(XALPHA[10], XMARKS[10]).replace(XALPHA[11], XMARKS[11]).replace(XALPHA[12], XMARKS[12]).replace(XALPHA[13], XMARKS[13]).replace(XALPHA[14], XMARKS[14]).replace(XALPHA[15], XMARKS[15]).replace(XALPHA[16], XMARKS[16]).replace(XALPHA[17], XMARKS[17]).replace(XALPHA[18], XMARKS[18]).replace(XALPHA[19], XMARKS[19]).replace(XALPHA[20], XMARKS[20]).replace(XALPHA[21], XMARKS[21]).replace(XALPHA[22], XMARKS[22]).replace(XALPHA[23], XMARKS[23]).replace(XALPHA[24], XMARKS[24]).replace(XALPHA[25], XMARKS[25]))

	XOUT = str(XTRANS.replace(XMARKS[0], XSHIFT[0]).replace(XMARKS[1], XSHIFT[1]).replace(XMARKS[2], XSHIFT[2]).replace(XMARKS[3], XSHIFT[3]).replace(XMARKS[4], XSHIFT[4]).replace(XMARKS[5], XSHIFT[5]).replace(XMARKS[6], XSHIFT[6]).replace(XMARKS[7], XSHIFT[7]).replace(XMARKS[8], XSHIFT[8]).replace(XMARKS[9], XSHIFT[9]).replace(XMARKS[10], XSHIFT[10]).replace(XMARKS[11], XSHIFT[11]).replace(XMARKS[12], XSHIFT[12]).replace(XMARKS[13], XSHIFT[13]).replace(XMARKS[14], XSHIFT[14]).replace(XMARKS[15], XSHIFT[15]).replace(XMARKS[16], XSHIFT[16]).replace(XMARKS[17], XSHIFT[17]).replace(XMARKS[18], XSHIFT[18]).replace(XMARKS[19], XSHIFT[19]).replace(XMARKS[20], XSHIFT[20]).replace(XMARKS[21], XSHIFT[21]).replace(XMARKS[22], XSHIFT[22]).replace(XMARKS[23], XSHIFT[23]).replace(XMARKS[24], XSHIFT[24]).replace(XMARKS[25], XSHIFT[25]))

	return(XOUT)

def unshift(XVAR):

	word = str(XVAR)

	XMARKS = list(['.00','.01','.02','.03','.04','.05','.06','.07','.08','.09','.10','.11','.12','.13','.14','.15','.16','.17','.18','.19','.20','.21','.22','.23','.24','.25'])

	XALPHA = list(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'])

	XSHIFT = list(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

	XTRANS = str(word.replace(XALPHA[0], XMARKS[0]).replace(XALPHA[1], XMARKS[1]).replace(XALPHA[2], XMARKS[2]).replace(XALPHA[3], XMARKS[3]).replace(XALPHA[4], XMARKS[4]).replace(XALPHA[5], XMARKS[5]).replace(XALPHA[6], XMARKS[6]).replace(XALPHA[7], XMARKS[7]).replace(XALPHA[8], XMARKS[8]).replace(XALPHA[9], XMARKS[9]).replace(XALPHA[10], XMARKS[10]).replace(XALPHA[11], XMARKS[11]).replace(XALPHA[12], XMARKS[12]).replace(XALPHA[13], XMARKS[13]).replace(XALPHA[14], XMARKS[14]).replace(XALPHA[15], XMARKS[15]).replace(XALPHA[16], XMARKS[16]).replace(XALPHA[17], XMARKS[17]).replace(XALPHA[18], XMARKS[18]).replace(XALPHA[19], XMARKS[19]).replace(XALPHA[20], XMARKS[20]).replace(XALPHA[21], XMARKS[21]).replace(XALPHA[22], XMARKS[22]).replace(XALPHA[23], XMARKS[23]).replace(XALPHA[24], XMARKS[24]).replace(XALPHA[25], XMARKS[25]))

	XOUT = str(XTRANS.replace(XMARKS[0], XSHIFT[0]).replace(XMARKS[1], XSHIFT[1]).replace(XMARKS[2], XSHIFT[2]).replace(XMARKS[3], XSHIFT[3]).replace(XMARKS[4], XSHIFT[4]).replace(XMARKS[5], XSHIFT[5]).replace(XMARKS[6], XSHIFT[6]).replace(XMARKS[7], XSHIFT[7]).replace(XMARKS[8], XSHIFT[8]).replace(XMARKS[9], XSHIFT[9]).replace(XMARKS[10], XSHIFT[10]).replace(XMARKS[11], XSHIFT[11]).replace(XMARKS[12], XSHIFT[12]).replace(XMARKS[13], XSHIFT[13]).replace(XMARKS[14], XSHIFT[14]).replace(XMARKS[15], XSHIFT[15]).replace(XMARKS[16], XSHIFT[16]).replace(XMARKS[17], XSHIFT[17]).replace(XMARKS[18], XSHIFT[18]).replace(XMARKS[19], XSHIFT[19]).replace(XMARKS[20], XSHIFT[20]).replace(XMARKS[21], XSHIFT[21]).replace(XMARKS[22], XSHIFT[22]).replace(XMARKS[23], XSHIFT[23]).replace(XMARKS[24], XSHIFT[24]).replace(XMARKS[25], XSHIFT[25]))

	return(XOUT.lower())