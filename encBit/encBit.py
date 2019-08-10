text = input("Enter Text : ")
ky = abs(int(input("Enter Key (Max255Min1) : ")))
bitler = []
hsh = []
Openhsh = []
encFile = open("encF.txt","w")
#variable
if ky <=255:
    for i in text.upper():
        bitler.append(ord(i))
    for j in bitler:
        hsh.append(j^ky)
    for k in hsh:
        Openhsh.append(chr(k))
    print("Hash : {}  ,  {}".format(Openhsh,hsh))
    for l in Openhsh:
        encFile.write(str(l))
    encFile.close()
else:
    print("Key too long")