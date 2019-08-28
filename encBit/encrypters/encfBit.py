import encLib
import sys
import os
fname = (sys.argv[1])
key = abs(int((sys.argv[2])))
encrypter = encLib.eLib(key)
#Terminal inputs
os.chdir("../Texts/")
file = open(fname,"r")
fCont = file.read()
file.close()
#file read
hash = encrypter.AsciiToText(encrypter.encryption(encrypter.TextToAscii(fCont)))
#encrypt
os.chdir("../ENCTexts/")
wf = open("ENC"+fname[0:3]+".data","w")
for j in hash:
    wf.write(j)
wf.close()
#file wiriting
