import os
import encLib
text = input("Text:")
ky = abs(int(input("Key (Max255Min1):")))
#variable
Ascii = encLib.TextToAscii(text)
CrAscii = encLib.encryption(Ascii,ky)
Hash = encLib.AsciiToText(CrAscii)
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
