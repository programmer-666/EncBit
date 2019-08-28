import os
import encLib
text = input("Text:")
ky = abs(int(input("Key (Max255Min1):")))
encrypter = encLib.eLib(ky)
#variable
Hash = encrypter.AsciiToText(encrypter.encryption(encrypter.TextToAscii(text)))
sw = input("Save a file(y/n):")
if sw == "y":
	os.chdir("../ENCTexts/")
	fname = input("File Name(x.txt):")
	encLib.WriteAFile("ENC"+fname,Hash)
elif sw == "n":
	for i in Hash:
		print(i,end="")
else:
	pass
