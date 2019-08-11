text = input("Enter Text : ")
ky = abs(int(input("Enter Key (Max255Min1) : ")))
#variable
def TextToAscii(Text):
    lst = []
    for i in Text.upper():
        lst.append(ord(i))
    return lst
def xor(BitList,Key):
    lst = []
    for i in BitList:
        lst.append(i^Key)
    return lst
def AsciiToText(AscLst):
    lst = []
    for i in AscLst:
        lst.append(chr(i))
    return lst
def WriteAFile(fname,format,content):
    File = open(fname+"."+format,"w")
    for i in content:
        File.write(i)
    File.close()
#functions
Ascii = TextToAscii(text)
CrAscii = xor(Ascii,ky)
Hash = AsciiToText(CrAscii)
print(Hash)
WriteAFile("encF","txt",Hash)
