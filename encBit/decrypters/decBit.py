import os
import encLib
text = input("Text:")
ky = abs(int(input("Key (Max255Min1):")))
decrypter = encLib.eLib(ky)
#variable
mesage = decrypter.AsciiToText(decrypter.encryption(decrypter.TextToAscii(text)))
sw = input("Save a file(y/n):")
if sw == "y":
	os.chdir("../ENCTexts/")
	fname = input("File Name(x.txt):")
	encLib.WriteAFile("ENC"+fname,mesage)
elif sw == "n":
	for i in mesage:
		print(i,end="")
else:
	pass
