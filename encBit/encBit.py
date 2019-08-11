text = input("Enter Text : ")
ky = abs(int(input("Enter Key (Max255Min1) : ")))
bitler = []
hash = []
Openhsh = []
encFile = open("encF.txt","w")
#variable
""" Islemler
if ky <=255:
    for i in text.upper():
        bitler.append(ord(i))
    for j in bitler:
        hash.append(j^ky)

    for k in hash:
        Openhsh.append(chr(k))
        print("Hash : {}  ,  {}".format(Openhsh,ha  sh))
    for l in Openhsh:
        encFile.write(str(l))
    encFile.close()
else:
    print("Key too long")
"""
#functions
def TextToAscii(Text):
    lst = []
    for i in Text.upper():
        lst.append(ord(i))
    return lst
