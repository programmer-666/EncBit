import sys
text = sys.argv[1]
ky = abs(int(sys.argv[2]))
filename = sys.argv[3]
fileformat = sys.argv[4]
#variable
def TextToAscii(Text):
    lst = []
    for i in Text.upper():
        lst.append(ord(i))
    return lst
def encryption(BitList,Key):
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
CrAscii = encryption(Ascii,ky)
Hash = AsciiToText(CrAscii)
print(Hash)
WriteAFile(filename,fileformat,Hash)
