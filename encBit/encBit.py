import encLib
text = input("Text:")
ky = abs(int(input("Key (Max255Min1):")))
#variable
Ascii = encLib.TextToAscii(text)
CrAscii = encLib.encryption(Ascii,ky)
Hash = encLib.AsciiToText(CrAscii)
sw = input("Save a file(y/n):")
if sw == "y":
	fname = input("File Name:")
	encLib.WriteAFile(fname,"txt",Hash)
elif sw == "n":
	for i in Hash:
		print(i,end="")
else:
	pass
print("\n")
