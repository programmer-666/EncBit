import encLib
import sys
import os
fname = (sys.argv[1])
key = abs(int((sys.argv[2])))
decrypter = encLib.eLib(key)
#Terminal inputs
os.chdir("../ENCTexts/")
file = open(fname,"r")
fCont = file.read()
file.close()
#file read
hash = decrypter.AsciiToText(decrypter.encryption(decrypter.TextToAscii(fCont)))
#encrypt
os.chdir("../Texts/")
wf = open("DEC"+fname[3:],"w")
for j in hash:
    wf.write(j)
wf.close()
#file wiriting
